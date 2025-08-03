class InsuranceAssistant {
    constructor() {
        this.apiKey = 'sk-d3b271ed56894ec09de13f4d6a5737e2';
        this.companyInfo = '中意人寿保险有限公司是中意两国合资企业，致力于为尊贵客户提供全面的保险保障和财富管理服务。';
        
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        // 分析按钮
        const analyzeBtn = document.getElementById('analyzeBtn');
        if (analyzeBtn) {
            analyzeBtn.addEventListener('click', () => this.analyzeCustomer());
        }

        // 清除按钮
        const clearBtn = document.getElementById('clearBtn');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => this.clearAnalysis());
        }

        // 分享按钮
        const shareBtn = document.getElementById('shareBtn');
        if (shareBtn) {
            shareBtn.addEventListener('click', () => this.shareAnalysis());
        }

        // 键盘快捷键
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter') {
                this.analyzeCustomer();
            }
        });
    }

    async analyzeCustomer() {
        const customerInput = document.getElementById('customerInput');
        const analysisResult = document.getElementById('analysisResult');
        const analyzeBtn = document.getElementById('analyzeBtn');
        const loadingSpinner = document.getElementById('loadingSpinner');
        
        if (!customerInput || !customerInput.value.trim()) {
            this.showNotification('请输入客户信息', 'error');
            return;
        }
        
        // 显示加载状态
        if (analyzeBtn) analyzeBtn.disabled = true;
        if (loadingSpinner) loadingSpinner.style.display = 'flex';
        if (analysisResult) analysisResult.innerHTML = '';
        
        try {
            const prompt = this.buildAnalysisPrompt(customerInput.value);
            const response = await this.callDeepSeekAPI(prompt);
            
            if (analysisResult) {
                analysisResult.innerHTML = this.formatAnalysisResult(response);
            }
            
        } catch (error) {
            console.error('分析失败:', error);
            if (analysisResult) {
                analysisResult.innerHTML = `
                    <div class="error-message">
                        <i class="fas fa-exclamation-triangle"></i>
                        <p>分析失败，请检查网络连接</p>
                        <small>${error.message}</small>
                    </div>
                `;
            }
        } finally {
            // 隐藏加载状态
            if (analyzeBtn) analyzeBtn.disabled = false;
            if (loadingSpinner) loadingSpinner.style.display = 'none';
        }
    }

    clearAnalysis() {
        const customerInput = document.getElementById('customerInput');
        const analysisResult = document.getElementById('analysisResult');
        
        if (customerInput) customerInput.value = '';
        if (analysisResult) analysisResult.innerHTML = '';
        
        this.showNotification('已清除分析结果', 'info');
    }

    shareAnalysis() {
        const customerInput = document.getElementById('customerInput');
        const analysisResult = document.getElementById('analysisResult');
        
        if (!customerInput || !analysisResult || !customerInput.value.trim()) {
            this.showNotification('请先进行客户分析', 'error');
            return;
        }
        
        // 复制到剪贴板
        const shareText = `客户信息：\n${customerInput.value}\n\n分析结果：\n${analysisResult.textContent}`;
        
        if (navigator.clipboard) {
            navigator.clipboard.writeText(shareText).then(() => {
                this.showNotification('分析结果已复制到剪贴板', 'success');
            }).catch(() => {
                this.fallbackCopyToClipboard(shareText);
            });
        } else {
            this.fallbackCopyToClipboard(shareText);
        }
    }
    
    fallbackCopyToClipboard(text) {
        const textArea = document.createElement('textarea');
        textArea.value = text;
        document.body.appendChild(textArea);
        textArea.select();
        try {
            document.execCommand('copy');
            this.showNotification('分析结果已复制到剪贴板', 'success');
        } catch (err) {
            this.showNotification('复制失败，请手动复制', 'error');
        }
        document.body.removeChild(textArea);
    }

    buildAnalysisPrompt(customerInfo) {
        return `作为${this.companyInfo}的专业保险顾问，请分析以下客户信息，并提供详细的保险需求分析和产品推荐建议：\n\n客户信息：\n${customerInfo}\n\n请从以下维度进行分析：\n1. 客户基本画像（年龄、职业、收入水平、家庭状况）\n2. 风险承受能力评估\n3. 保险需求分析（保障缺口、优先级排序）\n4. 产品推荐建议（具体产品类型、保额建议）\n5. 销售策略建议（沟通要点、关注重点）\n\n请确保分析专业、准确，并提供可操作的建议。`;
    }

    async callDeepSeekAPI(prompt) {
        const response = await fetch('https://api.deepseek.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.apiKey}`
            },
            body: JSON.stringify({
                model: 'deepseek-chat',
                messages: [{
                    role: 'user',
                    content: prompt
                }],
                temperature: 0.7,
                max_tokens: 2000
            })
        });
        
        if (!response.ok) {
            throw new Error(`API请求失败: ${response.status}`);
        }
        
        const data = await response.json();
        return data.choices[0].message.content;
    }

    formatAnalysisResult(content) {
        // 简单的格式化处理
        const formatted = content
            .replace(/\n\n/g, '</p><p>')
            .replace(/\n/g, '<br>')
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>');
        
        return `<div class="analysis-content"><p>${formatted}</p></div>`;
    }

    showNotification(message, type = 'info') {
        // 创建通知元素
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <span>${message}</span>
                <button class="notification-close">&times;</button>
            </div>
        `;
        
        // 添加到页面
        document.body.appendChild(notification);
        
        // 显示动画
        setTimeout(() => notification.classList.add('show'), 100);
        
        // 自动隐藏
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 3000);
        
        // 点击关闭
        notification.querySelector('.notification-close').addEventListener('click', () => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        });
    }
}

// 初始化应用
document.addEventListener('DOMContentLoaded', () => {
    new InsuranceAssistant();
});