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