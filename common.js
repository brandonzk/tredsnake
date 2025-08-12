/* 通用JavaScript文件 - 减少重复代码 */

// 背景图片数组
const backgroundImages = [
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (21).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (23).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (24).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (25).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (26).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (27).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (29).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (30).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (31).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (32).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (33).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (39).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (42).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (43).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (44).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (45).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (46).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (47).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (48).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (49).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (50).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (51).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (54).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (55).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (56).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (57).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (58).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (59).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (60).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (61).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (62).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (63).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (64).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (65).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (66).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (67).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (68).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (69).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (70).png',
    '中意人寿/中意产品介绍/banner/Appeal for Unblocking Account (71).png'
];

// 将背景图片数组暴露到全局作用域
window.backgroundImages = backgroundImages;

// 随机背景切换功能
function changeBackgroundImage() {
    const randomIndex = Math.floor(Math.random() * backgroundImages.length);
    const selectedImage = backgroundImages[randomIndex];
    const pageBanner = document.querySelector('.page-banner');
    if (pageBanner) {
        pageBanner.style.backgroundImage = `url('${selectedImage}')`;
    }
}

// 通知功能
function showNotification(message, type = 'info') {
    const notification = document.getElementById('notification');
    if (!notification) return;
    
    notification.textContent = message;
    notification.className = `notification ${type} show`;
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

// 页面初始化
function initializePage() {
    // 设置初始背景
    changeBackgroundImage();
    
    // 设置背景切换间隔（30秒）
    setInterval(changeBackgroundImage, 30000);
    
    // 预加载背景图片以提升性能
    preloadBackgroundImages();
}

// 预加载背景图片
function preloadBackgroundImages() {
    backgroundImages.forEach(imagePath => {
        const img = new Image();
        img.src = imagePath;
    });
}

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', initializePage);

// 导出函数供其他脚本使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        changeBackgroundImage,
        showNotification,
        initializePage
    };
}

// 统一设置管理器
const SettingsManager = {
    // 切换设置面板
    toggleSettings: function() {
        const settingsPanel = document.getElementById('settingsPanel'); // 应该是 'settingsPanel' 而不是 'settings-panel'
        if (settingsPanel) {
            settingsPanel.classList.toggle('show');
        }
    },
    
    // 加载设置
    loadSettings: function() {
        const saved = localStorage.getItem('zhongyi-settings');
        if (saved) {
            try {
                return JSON.parse(saved);
            } catch (e) {
                console.error('设置加载失败:', e);
            }
        }
        return {
            apiKey: '',
            model: 'gpt-4',
            temperature: 0.7
        };
    },
    
    // 保存设置
    saveSettings: function(settings) {
        try {
            localStorage.setItem('zhongyi-settings', JSON.stringify(settings));
            showNotification('设置已保存', 'success');
        } catch (e) {
            console.error('设置保存失败:', e);
            showNotification('设置保存失败', 'error');
        }
    }
};

// 将设置管理器暴露到全局
window.SettingsManager = SettingsManager;
window.toggleSettings = SettingsManager.toggleSettings;
window.loadSettings = SettingsManager.loadSettings;
window.saveSettings = SettingsManager.saveSettings;