# AI产品整理标准输出格式 - 独立版

## 使用说明

本文档提供了保险产品信息的标准化整理格式，可以发送给任何AI助手进行产品信息的结构化整理。

### 使用方法
1. 将产品PDF或文档内容提供给AI
2. 要求AI按照以下JSON格式输出产品信息
3. 将输出结果保存为JSON文件，上传到系统中

---

## 标准输出格式

请按照以下JSON格式整理产品信息：

```json
{
  "productInfo": {
    "productName": "产品全称",
    "productType": "产品类型（如：终身寿险、重疾险、医疗险等）",
    "company": "保险公司名称",
    "lastUpdated": "YYYY-MM-DD",
    "version": "产品版本号"
  },
  "coreFeatures": {
    "mainBenefits": [
      "主要保障责任1",
      "主要保障责任2",
      "主要保障责任3"
    ],
    "keyHighlights": [
      "产品亮点1",
      "产品亮点2",
      "产品亮点3"
    ],
    "uniqueAdvantages": [
      "独特优势1",
      "独特优势2"
    ]
  },
  "coverageDetails": {
    "basicCoverage": {
      "deathBenefit": "身故保险金详情",
      "disabilityBenefit": "伤残保险金详情",
      "criticalIllness": "重疾保障详情",
      "medicalExpense": "医疗费用保障详情",
      "other": "其他保障详情"
    },
    "optionalCoverage": [
      {
        "name": "可选保障名称",
        "description": "保障描述",
        "premium": "保费说明"
      }
    ],
    "exclusions": [
      "免责条款1",
      "免责条款2"
    ]
  },
  "eligibilityRules": {
    "ageRange": {
      "min": "最小投保年龄",
      "max": "最大投保年龄"
    },
    "healthRequirements": [
      "健康告知要求1",
      "健康告知要求2"
    ],
    "occupationLimits": [
      "职业限制说明"
    ],
    "coverageAmount": {
      "min": "最低保额",
      "max": "最高保额",
      "rules": "保额规则说明"
    }
  },
  "premiumInfo": {
    "paymentMethods": [
      "缴费方式1（如：趸交、年交等）",
      "缴费方式2"
    ],
    "paymentPeriods": [
      "缴费期间选项1",
      "缴费期间选项2"
    ],
    "premiumCalculation": "保费计算方式说明",
    "discounts": [
      "优惠政策1",
      "优惠政策2"
    ]
  },
  "targetCustomers": {
    "primaryTarget": {
      "ageGroup": "主要目标年龄段",
      "incomeLevel": "收入水平",
      "familyStatus": "家庭状况",
      "riskProfile": "风险偏好"
    },
    "scenarios": [
      {
        "situation": "适用场景1",
        "reason": "推荐理由",
        "configuration": "配置建议"
      },
      {
        "situation": "适用场景2",
        "reason": "推荐理由",
        "configuration": "配置建议"
      }
    ]
  },
  "salesTalkingPoints": {
    "openingLines": [
      "开场话术1",
      "开场话术2"
    ],
    "benefitExplanation": [
      "利益点说明1",
      "利益点说明2"
    ],
    "objectionHandling": [
      {
        "objection": "常见异议1",
        "response": "应对话术"
      },
      {
        "objection": "常见异议2",
        "response": "应对话术"
      }
    ],
    "closingTechniques": [
      "成交话术1",
      "成交话术2"
    ]
  },
  "productCombinations": {
    "recommendedPairs": [
      {
        "product": "搭配产品名称",
        "reason": "搭配理由",
        "benefit": "组合优势"
      }
    ],
    "portfolioSuggestions": [
      {
        "customerType": "客户类型",
        "products": ["产品1", "产品2"],
        "allocation": "配置比例建议"
      }
    ]
  },
  "riskWarnings": {
    "investmentRisks": [
      "投资风险提示1",
      "投资风险提示2"
    ],
    "policyRisks": [
      "保单风险提示1",
      "保单风险提示2"
    ],
    "marketRisks": [
      "市场风险提示1"
    ]
  },
  "faq": [
    {
      "question": "常见问题1",
      "answer": "详细回答"
    },
    {
      "question": "常见问题2",
      "answer": "详细回答"
    }
  ],
  "updateLog": [
    {
      "date": "YYYY-MM-DD",
      "version": "版本号",
      "changes": "更新内容说明"
    }
  ]
}
```

---

## 输出要求

1. **完整性**：确保所有字段都有内容，如果某项不适用，请填写"不适用"或"无"
2. **准确性**：信息必须来源于官方产品文档，不得编造
3. **结构化**：严格按照JSON格式输出，确保语法正确
4. **中文输出**：所有内容使用简体中文
5. **专业性**：使用保险行业专业术语，保持表述准确

---

## 示例输出

```json
{
  "productInfo": {
    "productName": "中意一生挚爱（荣耀版）终身寿险（分红型）",
    "productType": "终身寿险（分红型）",
    "company": "中意人寿保险有限公司",
    "lastUpdated": "2024-01-15",
    "version": "2024版"
  },
  "coreFeatures": {
    "mainBenefits": [
      "终身身故保障",
      "年度分红收益",
      "现金价值积累"
    ],
    "keyHighlights": [
      "保额可达500万",
      "分红抵御通胀",
      "现金价值稳定增长"
    ],
    "uniqueAdvantages": [
      "核保条件相对宽松",
      "适合高净值客户资产传承"
    ]
  }
  // ... 其他字段按格式填写
}
```

---

## 使用提示

- 将此格式发送给任何AI助手，要求其按此格式整理产品信息
- 整理完成后，将JSON内容保存为 `.json` 文件
- 文件命名建议：`产品名称_YYYYMMDD.json`
- 上传到系统后即可离线使用，避免重复API调用

---

**注意**：请确保AI助手严格按照此JSON格式输出，任何格式错误都可能导致系统无法正确解析。