#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中意保险文件管理API服务
提供文件管理、重命名、上传到数据库等功能
"""

import os
import json
import sqlite3
import shutil
from datetime import datetime
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 配置
CONFIG = {
    'ZHONGYI_FOLDER': '/Users/zhaoke/Desktop/zhongyi-ai-engine/中意人寿/中意产品介绍/zhongyi',
    'DATABASE_PATH': '/Users/zhaoke/Desktop/zhongyi-ai-engine/zhongyi_files.db',
    'ALLOWED_EXTENSIONS': {'.md', '.txt', '.pdf'},
    'MAX_FILE_SIZE': 10 * 1024 * 1024,  # 10MB
}

def init_database():
    """初始化数据库"""
    conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
    cursor = conn.cursor()
    
    # 创建文件表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL UNIQUE,
            original_name TEXT NOT NULL,
            content TEXT,
            file_size INTEGER,
            upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            file_type TEXT,
            status TEXT DEFAULT 'active'
        )
    ''')
    
    # 创建操作日志表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS operation_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation_type TEXT NOT NULL,
            filename TEXT,
            details TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'success'
        )
    ''')
    
    conn.commit()
    conn.close()

def log_operation(operation_type, filename=None, details=None, status='success'):
    """记录操作日志"""
    conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO operation_logs (operation_type, filename, details, status)
        VALUES (?, ?, ?, ?)
    ''', (operation_type, filename, details, status))
    
    conn.commit()
    conn.close()

def get_file_info(filepath):
    """获取文件信息"""
    try:
        stat = os.stat(filepath)
        return {
            'size': stat.st_size,
            'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            'created': datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        }
    except OSError:
        return {'size': 0, 'modified': 'Unknown', 'created': 'Unknown'}

@app.route('/api/files', methods=['GET'])
def get_files():
    """获取zhongyi文件夹中的所有文件"""
    try:
        zhongyi_path = Path(CONFIG['ZHONGYI_FOLDER'])
        
        if not zhongyi_path.exists():
            return jsonify({'error': 'zhongyi文件夹不存在'}), 404
        
        files = []
        for file_path in zhongyi_path.iterdir():
            if file_path.is_file() and file_path.suffix in CONFIG['ALLOWED_EXTENSIONS']:
                file_info = get_file_info(file_path)
                files.append({
                    'name': file_path.name,
                    'size': f"{file_info['size'] / 1024:.1f} KB",
                    'modified': file_info['modified'],
                    'type': file_path.suffix,
                    'path': str(file_path)
                })
        
        # 按文件名排序
        files.sort(key=lambda x: x['name'])
        
        log_operation('list_files', details=f'返回{len(files)}个文件')
        return jsonify({'files': files, 'count': len(files)})
        
    except Exception as e:
        log_operation('list_files', details=str(e), status='error')
        return jsonify({'error': f'获取文件列表失败: {str(e)}'}), 500

@app.route('/api/files/rename', methods=['POST'])
def rename_file():
    """重命名文件"""
    try:
        data = request.get_json()
        old_name = data.get('old_name')
        new_name = data.get('new_name')
        
        if not old_name or not new_name:
            return jsonify({'error': '缺少文件名参数'}), 400
        
        # 确保新文件名有正确的扩展名
        if not any(new_name.endswith(ext) for ext in CONFIG['ALLOWED_EXTENSIONS']):
            new_name += '.md'  # 默认添加.md扩展名
        
        zhongyi_path = Path(CONFIG['ZHONGYI_FOLDER'])
        old_path = zhongyi_path / old_name
        new_path = zhongyi_path / new_name
        
        if not old_path.exists():
            return jsonify({'error': f'文件 {old_name} 不存在'}), 404
        
        if new_path.exists():
            return jsonify({'error': f'文件 {new_name} 已存在'}), 409
        
        # 执行重命名
        old_path.rename(new_path)
        
        # 更新数据库中的记录（如果存在）
        conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE files SET filename = ?, last_modified = CURRENT_TIMESTAMP
            WHERE filename = ?
        ''', (new_name, old_name))
        conn.commit()
        conn.close()
        
        log_operation('rename_file', old_name, f'重命名为: {new_name}')
        return jsonify({'message': f'文件已重命名: {old_name} → {new_name}'})
        
    except Exception as e:
        log_operation('rename_file', old_name, str(e), 'error')
        return jsonify({'error': f'重命名失败: {str(e)}'}), 500

@app.route('/api/files/upload', methods=['POST'])
def upload_file_to_db():
    """上传文件内容到数据库"""
    try:
        data = request.get_json()
        filename = data.get('filename')
        
        if not filename:
            return jsonify({'error': '缺少文件名参数'}), 400
        
        zhongyi_path = Path(CONFIG['ZHONGYI_FOLDER'])
        file_path = zhongyi_path / filename
        
        if not file_path.exists():
            return jsonify({'error': f'文件 {filename} 不存在'}), 404
        
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        file_info = get_file_info(file_path)
        
        # 保存到数据库
        conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO files 
            (filename, original_name, content, file_size, file_type, last_modified)
            VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
        ''', (filename, filename, content, file_info['size'], file_path.suffix))
        
        conn.commit()
        conn.close()
        
        log_operation('upload_file', filename, f'上传到数据库，大小: {file_info["size"]} bytes')
        return jsonify({'message': f'文件 {filename} 已上传到数据库'})
        
    except Exception as e:
        log_operation('upload_file', filename, str(e), 'error')
        return jsonify({'error': f'上传失败: {str(e)}'}), 500

@app.route('/api/files/upload-all', methods=['POST'])
def upload_all_files():
    """批量上传所有文件到数据库"""
    try:
        zhongyi_path = Path(CONFIG['ZHONGYI_FOLDER'])
        
        if not zhongyi_path.exists():
            return jsonify({'error': 'zhongyi文件夹不存在'}), 404
        
        uploaded_count = 0
        errors = []
        
        for file_path in zhongyi_path.iterdir():
            if file_path.is_file() and file_path.suffix in CONFIG['ALLOWED_EXTENSIONS']:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    file_info = get_file_info(file_path)
                    
                    conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
                    cursor = conn.cursor()
                    
                    cursor.execute('''
                        INSERT OR REPLACE INTO files 
                        (filename, original_name, content, file_size, file_type, last_modified)
                        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                    ''', (file_path.name, file_path.name, content, file_info['size'], file_path.suffix))
                    
                    conn.commit()
                    conn.close()
                    
                    uploaded_count += 1
                    
                except Exception as e:
                    errors.append(f'{file_path.name}: {str(e)}')
        
        log_operation('upload_all', details=f'批量上传{uploaded_count}个文件')
        
        result = {'uploaded_count': uploaded_count}
        if errors:
            result['errors'] = errors
        
        return jsonify(result)
        
    except Exception as e:
        log_operation('upload_all', details=str(e), status='error')
        return jsonify({'error': f'批量上传失败: {str(e)}'}), 500

@app.route('/api/files/delete', methods=['DELETE'])
def delete_file():
    """删除文件"""
    try:
        data = request.get_json()
        filename = data.get('filename')
        
        if not filename:
            return jsonify({'error': '缺少文件名参数'}), 400
        
        zhongyi_path = Path(CONFIG['ZHONGYI_FOLDER'])
        file_path = zhongyi_path / filename
        
        if not file_path.exists():
            return jsonify({'error': f'文件 {filename} 不存在'}), 404
        
        # 删除文件
        file_path.unlink()
        
        # 从数据库中删除记录
        conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
        cursor = conn.cursor()
        cursor.execute('DELETE FROM files WHERE filename = ?', (filename,))
        conn.commit()
        conn.close()
        
        log_operation('delete_file', filename, '文件已删除')
        return jsonify({'message': f'文件 {filename} 已删除'})
        
    except Exception as e:
        log_operation('delete_file', filename, str(e), 'error')
        return jsonify({'error': f'删除失败: {str(e)}'}), 500

@app.route('/api/files/new', methods=['POST'])
def upload_new_file():
    """上传新文件"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': '没有文件'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        # 检查文件扩展名
        filename = secure_filename(file.filename)
        file_ext = Path(filename).suffix
        
        if file_ext not in CONFIG['ALLOWED_EXTENSIONS']:
            return jsonify({'error': f'不支持的文件格式: {file_ext}'}), 400
        
        # 检查文件大小
        file.seek(0, 2)  # 移动到文件末尾
        file_size = file.tell()
        file.seek(0)  # 重置到文件开头
        
        if file_size > CONFIG['MAX_FILE_SIZE']:
            return jsonify({'error': '文件太大'}), 400
        
        # 保存文件
        zhongyi_path = Path(CONFIG['ZHONGYI_FOLDER'])
        zhongyi_path.mkdir(parents=True, exist_ok=True)
        
        file_path = zhongyi_path / filename
        
        # 如果文件已存在，添加序号
        counter = 1
        original_stem = file_path.stem
        while file_path.exists():
            file_path = zhongyi_path / f"{original_stem}_{counter}{file_ext}"
            counter += 1
        
        file.save(str(file_path))
        
        # 读取内容并保存到数据库
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO files 
            (filename, original_name, content, file_size, file_type)
            VALUES (?, ?, ?, ?, ?)
        ''', (file_path.name, filename, content, file_size, file_ext))
        
        conn.commit()
        conn.close()
        
        log_operation('upload_new', file_path.name, f'新文件上传，大小: {file_size} bytes')
        return jsonify({'message': f'文件 {file_path.name} 上传成功'})
        
    except Exception as e:
        log_operation('upload_new', details=str(e), status='error')
        return jsonify({'error': f'上传失败: {str(e)}'}), 500

@app.route('/api/database/status', methods=['GET'])
def get_database_status():
    """获取数据库状态"""
    try:
        conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
        cursor = conn.cursor()
        
        # 获取文件数量
        cursor.execute('SELECT COUNT(*) FROM files WHERE status = "active"')
        file_count = cursor.fetchone()[0]
        
        # 获取最后上传时间
        cursor.execute('SELECT MAX(upload_time) FROM files')
        last_upload = cursor.fetchone()[0]
        
        # 获取数据库大小
        db_size = os.path.getsize(CONFIG['DATABASE_PATH']) if os.path.exists(CONFIG['DATABASE_PATH']) else 0
        
        conn.close()
        
        return jsonify({
            'connected': True,
            'file_count': file_count,
            'last_upload': last_upload,
            'database_size': f"{db_size / 1024:.1f} KB"
        })
        
    except Exception as e:
        return jsonify({
            'connected': False,
            'error': str(e)
        }), 500

@app.route('/api/database/clear', methods=['DELETE'])
def clear_database():
    """清空数据库"""
    try:
        conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM files')
        cursor.execute('DELETE FROM operation_logs')
        
        conn.commit()
        conn.close()
        
        log_operation('clear_database', details='数据库已清空')
        return jsonify({'message': '数据库已清空'})
        
    except Exception as e:
        log_operation('clear_database', details=str(e), status='error')
        return jsonify({'error': f'清空失败: {str(e)}'}), 500

@app.route('/api/logs', methods=['GET'])
def get_operation_logs():
    """获取操作日志"""
    try:
        limit = request.args.get('limit', 50, type=int)
        
        conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT operation_type, filename, details, timestamp, status
            FROM operation_logs
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))
        
        logs = []
        for row in cursor.fetchall():
            logs.append({
                'operation_type': row[0],
                'filename': row[1],
                'details': row[2],
                'timestamp': row[3],
                'status': row[4]
            })
        
        conn.close()
        
        return jsonify({'logs': logs})
        
    except Exception as e:
        return jsonify({'error': f'获取日志失败: {str(e)}'}), 500

@app.route('/api/export', methods=['GET'])
def export_data():
    """导出数据"""
    try:
        conn = sqlite3.connect(CONFIG['DATABASE_PATH'])
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM files WHERE status = "active"')
        files = cursor.fetchall()
        
        cursor.execute('SELECT * FROM operation_logs ORDER BY timestamp DESC LIMIT 100')
        logs = cursor.fetchall()
        
        conn.close()
        
        export_data = {
            'export_time': datetime.now().isoformat(),
            'files': files,
            'logs': logs
        }
        
        log_operation('export_data', details=f'导出{len(files)}个文件和{len(logs)}条日志')
        return jsonify(export_data)
        
    except Exception as e:
        log_operation('export_data', details=str(e), status='error')
        return jsonify({'error': f'导出失败: {str(e)}'}), 500

@app.route('/')
def index():
    """主页"""
    return '''
    <h1>中意保险文件管理API</h1>
    <p>API服务正在运行</p>
    <ul>
        <li><a href="/api/files">获取文件列表</a></li>
        <li><a href="/api/database/status">数据库状态</a></li>
        <li><a href="/api/logs">操作日志</a></li>
    </ul>
    '''

if __name__ == '__main__':
    # 初始化数据库
    init_database()
    
    print("中意保险文件管理API服务启动中...")
    print(f"zhongyi文件夹路径: {CONFIG['ZHONGYI_FOLDER']}")
    print(f"数据库路径: {CONFIG['DATABASE_PATH']}")
    print("API服务地址: http://localhost:5000")
    
    # 启动Flask应用
    app.run(host='0.0.0.0', port=5001, debug=True)