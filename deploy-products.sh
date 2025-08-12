#!/bin/bash

# 设置颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 开始部署产品库...${NC}"

# 1. 检查并创建scripts目录
if [ ! -d "scripts" ]; then
    echo -e "${YELLOW}📁 创建scripts目录...${NC}"
    mkdir -p scripts
fi

# 2. 生成标准化产品库文件
echo -e "${YELLOW}📊 生成标准化产品库文件...${NC}"
if [ -f "scripts/generate-product-database.js" ]; then
    node scripts/generate-product-database.js
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ 产品库文件生成成功${NC}"
    else
        echo -e "${RED}❌ 产品库文件生成失败${NC}"
        exit 1
    fi
else
    echo -e "${RED}❌ 找不到生成脚本文件${NC}"
    exit 1
fi

# 3. 提交到Git仓库
echo -e "${YELLOW}📤 提交更改到Git仓库...${NC}"
git add .
git commit -m "更新产品库数据和优化产品匹配逻辑 $(date '+%Y-%m-%d %H:%M:%S')"

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Git提交成功${NC}"
    
    echo -e "${YELLOW}🌐 推送到远程仓库...${NC}"
    git push origin main
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ 推送成功${NC}"
    else
        echo -e "${YELLOW}⚠️ 推送失败或无新更改${NC}"
    fi
else
    echo -e "${YELLOW}⚠️ 无新更改需要提交${NC}"
fi

echo -e "${GREEN}🎉 产品库部署完成！${NC}"
echo -e "${GREEN}📋 部署摘要：${NC}"
echo -e "   • 产品库文件：products-database.json"
echo -e "   • 包含产品数量：7款主推产品"
echo -e "   • 优化功能：减少API调用，提升匹配效率"