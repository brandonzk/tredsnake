#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
中意赵珂保险AI智能引擎系统启动器
ZHONGYI Genesis AI Insurance Assistant System Launcher
"""

import os
import sys
import subprocess
import threading
import time
import webbrowser
from pathlib import Path

class ZhongyiSystemLauncher:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.api_process = None
        self.web_process = None
        self.api_port = 5001
        self.web_port = 8002
        
    def check_python(self):
        """检查Python环境"""
        try:
            import flask
            print("✓ Flask已安装")
        except ImportError:
            print("❌ Flask未安装，正在安装...")
            subprocess.run([sys.executable, "-m", "pip", "install", "flask", "flask-cors"])
            
    def start_api_server(self):
        """启动API服务器"""
        try:
            api_script = self.base_dir / "file-manager-api.py"
            if not api_script.exists():
                print(f"❌ API脚本不存在: {api_script}")
                return False
                
            print(f"🚀 启动API服务器 (端口 {self.api_port})...")
            self.api_process = subprocess.Popen(
                [sys.executable, str(api_script)],
                cwd=str(self.base_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # 等待API服务器启动
            time.sleep(3)
            
            if self.api_process.poll() is None:
                print("✓ API服务器启动成功")
                return True
            else:
                print("❌ API服务器启动失败")
                return False
                
        except Exception as e:
            print(f"❌ 启动API服务器时出错: {e}")
            return False
            
    def start_web_server(self):
        """启动Web服务器"""
        try:
            print(f"🌐 启动Web服务器 (端口 {self.web_port})...")
            self.web_process = subprocess.Popen(
                [sys.executable, "-m", "http.server", str(self.web_port)],
                cwd=str(self.base_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            # 等待Web服务器启动
            time.sleep(2)
            
            if self.web_process.poll() is None:
                print("✓ Web服务器启动成功")
                return True
            else:
                print("❌ Web服务器启动失败")
                return False
                
        except Exception as e:
            print(f"❌ 启动Web服务器时出错: {e}")
            return False
            
    def open_browser(self):
        """打开浏览器"""
        try:
            url = f"http://localhost:{self.web_port}/zhongyi-intelligence-platform.html"
            print(f"🌍 打开浏览器: {url}")
            webbrowser.open(url)
            return True
        except Exception as e:
            print(f"❌ 打开浏览器时出错: {e}")
            return False
            
    def cleanup(self):
        """清理进程"""
        print("\n🛑 正在关闭服务器...")
        
        if self.api_process and self.api_process.poll() is None:
            self.api_process.terminate()
            self.api_process.wait()
            print("✓ API服务器已关闭")
            
        if self.web_process and self.web_process.poll() is None:
            self.web_process.terminate()
            self.web_process.wait()
            print("✓ Web服务器已关闭")
            
    def run(self):
        """运行系统"""
        print("="*60)
        print("🏢 中意赵珂保险AI智能引擎系统")
        print("   ZHONGYI Genesis AI Insurance Assistant")
        print("="*60)
        
        try:
            # 检查Python环境
            self.check_python()
            
            # 启动API服务器
            if not self.start_api_server():
                print("❌ 系统启动失败：API服务器无法启动")
                return
                
            # 启动Web服务器
            if not self.start_web_server():
                print("❌ 系统启动失败：Web服务器无法启动")
                self.cleanup()
                return
                
            # 打开浏览器
            time.sleep(1)
            self.open_browser()
            
            print("\n" + "="*60)
            print("✅ 系统启动成功！")
            print(f"📱 访问地址: http://localhost:{self.web_port}/zhongyi-intelligence-platform.html")
            print(f"🔧 API地址: http://localhost:{self.api_port}")
            print("\n💡 使用说明:")
            print("   1. 系统已自动打开浏览器")
            print("   2. 可以开始使用AI智能保险顾问功能")
            print("   3. 按 Ctrl+C 退出系统")
            print("="*60)
            
            # 保持运行
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n👋 用户请求退出系统")
                
        except Exception as e:
            print(f"❌ 系统运行时出错: {e}")
        finally:
            self.cleanup()
            print("\n✅ 系统已安全退出")

def main():
    launcher = ZhongyiSystemLauncher()
    launcher.run()

if __name__ == "__main__":
    main()