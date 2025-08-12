const fs = require('fs');
const path = require('path');

// 中意人寿7款主推产品的标准化数据
const productsData = {
  "products": [
    {
      "productInfo": {
        "productName": "中意一生挚爱（荣耀版）终身寿险（分红型）",
        "productType": "终身寿险（分红型）",
        "company": "中意人寿保险有限公司",
        "lastUpdated": "2024-12-19",
        "version": "2024版"
      },
      "coreFeatures": {
        "mainBenefits": [
          "终身身故保障",
          "年度分红收益",
          "现金价值积累",
          "保单贷款功能"
        ],
        "keyHighlights": [
          "保额可达500万",
          "分红抵御通胀",
          "现金价值稳定增长",
          "灵活缴费方式"
        ],
        "uniqueAdvantages": [
          "荣耀版专享权益",
          "适合高净值客户资产传承"
        ]
      },
      "targetCustomers": {
        "primaryTarget": {
          "ageGroup": "25-55岁",
          "incomeLevel": "中高收入",
          "familyStatus": "已婚有子女",
          "riskProfile": "稳健型"
        },
        "scenarios": [
          {
            "situation": "财富传承规划",
            "reason": "终身保障+分红收益，实现财富保值增值",
            "configuration": "建议保额200-500万，20年缴费"
          }
        ]
      },
      "salesTalkingPoints": {
        "openingLines": [
          "您好，我想为您介绍一款能够实现财富传承的终身寿险产品",
          "这款产品不仅提供终身保障，还能通过分红实现财富增值"
        ],
        "benefitExplanation": [
          "终身保障让您的家人永远有依靠",
          "年度分红帮助您抵御通胀风险",
          "现金价值稳定增长，资金灵活运用"
        ]
      }
    },
    {
      "productInfo": {
        "productName": "中意悦享年年年金保险（分红型）",
        "productType": "年金保险（分红型）",
        "company": "中意人寿保险有限公司",
        "lastUpdated": "2024-12-19",
        "version": "2024版"
      },
      "coreFeatures": {
        "mainBenefits": [
          "稳定年金给付",
          "分红收益",
          "现金价值积累",
          "灵活领取方式"
        ],
        "keyHighlights": [
          "保证年金给付",
          "分红增值潜力",
          "多种领取方式",
          "适合养老规划"
        ]
      },
      "targetCustomers": {
        "primaryTarget": {
          "ageGroup": "30-50岁",
          "incomeLevel": "中等以上收入",
          "familyStatus": "关注养老规划",
          "riskProfile": "稳健保守型"
        }
      }
    },
    {
      "productInfo": {
        "productName": "中意康健一生重大疾病保险",
        "productType": "重大疾病保险",
        "company": "中意人寿保险有限公司",
        "lastUpdated": "2024-12-19",
        "version": "2024版"
      },
      "coreFeatures": {
        "mainBenefits": [
          "重大疾病保障",
          "轻症疾病保障",
          "中症疾病保障",
          "身故保障"
        ],
        "keyHighlights": [
          "覆盖120种重疾",
          "轻症中症多次赔付",
          "保额递增设计",
          "核保条件宽松"
        ]
      },
      "targetCustomers": {
        "primaryTarget": {
          "ageGroup": "20-50岁",
          "incomeLevel": "各收入层次",
          "familyStatus": "关注健康保障",
          "riskProfile": "各风险偏好"
        }
      }
    },
    {
      "productInfo": {
        "productName": "中意安康医疗保险",
        "productType": "医疗保险",
        "company": "中意人寿保险有限公司",
        "lastUpdated": "2024-12-19",
        "version": "2024版"
      },
      "coreFeatures": {
        "mainBenefits": [
          "住院医疗保障",
          "门诊医疗保障",
          "特殊疾病保障",
          "海外医疗保障"
        ],
        "keyHighlights": [
          "保额高达1000万",
          "0免赔额设计",
          "100%报销比例",
          "全球医疗网络"
        ]
      }
    },
    {
      "productInfo": {
        "productName": "中意守护一生定期寿险",
        "productType": "定期寿险",
        "company": "中意人寿保险有限公司",
        "lastUpdated": "2024-12-19",
        "version": "2024版"
      },
      "coreFeatures": {
        "mainBenefits": [
          "定期身故保障",
          "全残保障",
          "保费低廉",
          "核保简单"
        ],
        "keyHighlights": [
          "高保额低保费",
          "保障期间灵活",
          "适合家庭责任期",
          "核保条件宽松"
        ]
      }
    },
    {
      "productInfo": {
        "productName": "中意安心意外伤害保险",
        "productType": "意外伤害保险",
        "company": "中意人寿保险有限公司",
        "lastUpdated": "2024-12-19",
        "version": "2024版"
      },
      "coreFeatures": {
        "mainBenefits": [
          "意外身故保障",
          "意外伤残保障",
          "意外医疗保障",
          "交通意外保障"
        ],
        "keyHighlights": [
          "保费极低",
          "保障全面",
          "理赔快速",
          "适合全家投保"
        ]
      }
    },
    {
      "productInfo": {
        "productName": "中意财富传承终身寿险（万能型）",
        "productType": "终身寿险（万能型）",
        "company": "中意人寿保险有限公司",
        "lastUpdated": "2024-12-19",
        "version": "2024版"
      },
      "coreFeatures": {
        "mainBenefits": [
          "终身身故保障",
          "万能账户增值",
          "灵活缴费",
          "部分领取功能"
        ],
        "keyHighlights": [
          "保底利率保证",
          "缴费灵活自主",
          "账户透明管理",
          "适合高净值客户"
        ]
      }
    }
  ],
  "lastUpdated": new Date().toISOString().split('T')[0],
  "version": "1.0",
  "totalProducts": 7
};

// 生成产品库文件
function generateProductDatabase() {
  try {
    const outputPath = path.join(__dirname, '..', 'products-database.json');
    fs.writeFileSync(outputPath, JSON.stringify(productsData, null, 2), 'utf8');
    console.log(`✅ 产品库文件已生成: ${outputPath}`);
    console.log(`📊 包含 ${productsData.products.length} 个产品`);
    console.log(`📅 更新时间: ${productsData.lastUpdated}`);
  } catch (error) {
    console.error('❌ 生成产品库文件失败:', error);
    process.exit(1);
  }
}

// 执行生成
generateProductDatabase();