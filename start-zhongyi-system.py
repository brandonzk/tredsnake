#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中意保险文件管理系统启动脚本
一键启动API服务和打开文件管理页面
"""

import os
import sys
import time
import subprocess
import webbrowser
from pathlib import Path
import threading

def check_dependencies():
    """检查依赖包"""
    required_packages = ['flask', 'flask-cors']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"缺少依赖包: {', '.join(missing_packages)}")
        print("正在安装依赖包...")
        
        for package in missing_packages:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"✅ {package} 安装成功")
            except subprocess.CalledProcessError:
                print(f"❌ {package} 安装失败")
                return False
    
    return True

def check_zhongyi_folder():
    """检查zhongyi文件夹是否存在"""
    zhongyi_path = Path('/Users/zhaoke/Desktop/zhongyi-ai-engine/中意人寿/中意产品介绍/zhongyi')
    
    if not zhongyi_path.exists():
        print(f"警告: zhongyi文件夹不存在: {zhongyi_path}")
        print("请确保文件夹路径正确")
        return False
    
    # 检查文件夹中是否有文件
    files = list(zhongyi_path.glob('*.md'))
    print(f"发现 {len(files)} 个Markdown文件")
    
    return True

def start_api_server():
    """启动API服务器"""
    try:
        api_script = Path('/Users/zhaoke/Desktop/zhongyi-ai-engine/file-manager-api.py')
        
        if not api_script.exists():
            print(f"❌ API脚本不存在: {api_script}")
            return None
        
        print("🚀 启动API服务器...")
        process = subprocess.Popen(
            [sys.executable, str(api_script)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 等待服务器启动
        time.sleep(3)
        
        if process.poll() is None:
            print("✅ API服务器启动成功 (http://localhost:5001)")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ API服务器启动失败")
            print(f"错误信息: {stderr}")
            return None
            
    except Exception as e:
        print(f"❌ 启动API服务器时出错: {e}")
        return None

def start_web_server():
    """启动Web服务器"""
    try:
        print("🌐 启动Web服务器...")
        
        # 切换到项目目录
        project_dir = Path('/Users/zhaoke/Desktop/zhongyi-ai-engine')
        os.chdir(project_dir)
        
        # 启动HTTP服务器
        process = subprocess.Popen(
            [sys.executable, '-m', 'http.server', '8081'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 等待服务器启动
        time.sleep(2)
        
        if process.poll() is None:
            print("✅ Web服务器启动成功 (http://localhost:8081)")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Web服务器启动失败")
            print(f"错误信息: {stderr}")
            return None
            
    except Exception as e:
        print(f"❌ 启动Web服务器时出错: {e}")
        return None

def open_browser():
    """打开浏览器"""
    try:
        time.sleep(5)  # 等待服务器完全启动
        
        file_manager_url = 'http://localhost:8081/zhongyi-file-manager.html'
        
        print(f"🌍 打开文件管理页面: {file_manager_url}")
        webbrowser.open(file_manager_url)
        
        # 也可以打开产品展示页面
        # products_url = 'http://localhost:8081/zhongyi-products.html'
        # print(f"🌍 打开产品展示页面: {products_url}")
        # webbrowser.open(products_url)
        
    except Exception as e:
        print(f"❌ 打开浏览器时出错: {e}")

def main():
    """主函数"""
    print("="*60)
    print("🏢 中意保险文件管理系统启动器")
    print("📋 基于ChatGPT的智能文档管理平台")
    print("="*60)
    
    # 检查依赖
    print("\n📦 检查依赖包...")
    if not check_dependencies():
        print("❌ 依赖检查失败，请手动安装缺少的包")
        return
    
    # 检查zhongyi文件夹
    print("\n📁 检查zhongyi文件夹...")
    check_zhongyi_folder()
    
    # 启动API服务器
    print("\n🔧 启动后端服务...")
    api_process = start_api_server()
    
    if not api_process:
        print("❌ 无法启动API服务器，程序退出")
        return
    
    # 启动Web服务器
    print("\n🌐 启动前端服务...")
    web_process = start_web_server()
    
    if not web_process:
        print("❌ 无法启动Web服务器，程序退出")
        if api_process:
            api_process.terminate()
        return
    
    # 在新线程中打开浏览器
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    print("\n" + "="*60)
    print("🎉 系统启动成功！")
    print("")
    print("📊 服务状态:")
    print("   • API服务器: http://localhost:5001")
    print("   • Web服务器: http://localhost:8081")
    print("   • 文件管理: http://localhost:8081/zhongyi-file-manager.html")
    print("   • 产品展示: http://localhost:8081/zhongyi-products.html")
    print("")
    print("💡 功能说明:")
    print("   • 文件重命名和管理")
    print("   • 批量上传到数据库")
    print("   • 远程访问和手机操作")
    print("   • 操作日志记录")
    print("")
    print("⚠️  按 Ctrl+C 停止所有服务")
    print("="*60)
    
    try:
        # 保持程序运行
        while True:
            time.sleep(1)
            
            # 检查进程是否还在运行
            if api_process.poll() is not None:
                print("\n❌ API服务器意外停止")
                break
                
            if web_process.poll() is not None:
                print("\n❌ Web服务器意外停止")
                break
                
    except KeyboardInterrupt:
        print("\n\n🛑 正在停止服务...")
        
        if api_process:
            api_process.terminate()
            print("✅ API服务器已停止")
            
        if web_process:
            web_process.terminate()
            print("✅ Web服务器已停止")
            
        print("\n👋 感谢使用中意保险文件管理系统！")

if __name__ == '__main__':
    main()