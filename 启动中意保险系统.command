#!/bin/bash

# 中意保险文件管理系统启动脚本
# 双击此文件即可启动整个系统

# 设置脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 清屏并显示启动信息
clear
echo "================================================================"
echo "🏢 中意保险文件管理系统"
echo "📋 基于ChatGPT的智能文档管理平台"
echo "================================================================"
echo ""
echo "🚀 正在启动系统..."
echo ""

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3"
    echo "请先安装Python3: https://www.python.org/downloads/"
    echo ""
    echo "按任意键退出..."
    read -n 1
    exit 1
fi

# 检查启动脚本是否存在
if [ ! -f "start-zhongyi-system.py" ]; then
    echo "❌ 错误: 未找到启动脚本 start-zhongyi-system.py"
    echo "请确保所有文件都在正确位置"
    echo ""
    echo "按任意键退出..."
    read -n 1
    exit 1
fi

# 检查API脚本是否存在
if [ ! -f "file-manager-api.py" ]; then
    echo "❌ 错误: 未找到API脚本 file-manager-api.py"
    echo "请确保所有文件都在正确位置"
    echo ""
    echo "按任意键退出..."
    read -n 1
    exit 1
fi

# 检查HTML文件是否存在
if [ ! -f "zhongyi-file-manager.html" ]; then
    echo "❌ 错误: 未找到文件管理页面 zhongyi-file-manager.html"
    echo "请确保所有文件都在正确位置"
    echo ""
    echo "按任意键退出..."
    read -n 1
    exit 1
fi

# 检查zhongyi文件夹
ZHONGYI_PATH="$SCRIPT_DIR/中意人寿/中意产品介绍/zhongyi"
if [ ! -d "$ZHONGYI_PATH" ]; then
    echo "⚠️  警告: zhongyi文件夹不存在"
    echo "路径: $ZHONGYI_PATH"
    echo "系统将继续启动，但可能无法正常工作"
    echo ""
else
    FILE_COUNT=$(find "$ZHONGYI_PATH" -name "*.md" | wc -l)
    echo "✅ 发现zhongyi文件夹，包含 $FILE_COUNT 个Markdown文件"
    echo ""
fi

# 启动Python脚本
echo "🔧 启动系统服务..."
echo ""
python3 start-zhongyi-system.py

# 如果脚本退出，显示退出信息
echo ""
echo "================================================================"
echo "👋 中意保险文件管理系统已停止"
echo "================================================================"
echo ""
echo "按任意键关闭此窗口..."
read -n 1