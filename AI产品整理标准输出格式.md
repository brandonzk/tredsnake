# AI产品整理标准输出格式

## 产品基本信息
```json
{
  "productName": "产品全称",
  "productCode": "产品代码",
  "productType": "产品类型（如：终身寿险、重疾险、医疗险等）",
  "insuranceCompany": "中意人寿",
  "launchDate": "上市时间",
  "status": "销售状态（在售/停售）"
}
```

## 核心特色
```json
{
  "keyFeatures": [
    "特色1：具体描述",
    "特色2：具体描述",
    "特色3：具体描述"
  ],
  "uniqueSellingPoints": [
    "独特卖点1",
    "独特卖点2",
    "独特卖点3"
  ]
}
```

## 保障责任
```json
{
  "coverageDetails": {
    "mainCoverage": {
      "name": "主要保障名称",
      "description": "保障描述",
      "payoutCondition": "给付条件",
      "payoutAmount": "给付金额计算方式"
    },
    "additionalCoverage": [
      {
        "name": "附加保障名称",
        "description": "保障描述",
        "optional": true/false
      }
    ]
  }
}
```

## 投保规则
```json
{
  "eligibility": {
    "ageRange": {
      "min": "最小投保年龄",
      "max": "最大投保年龄"
    },
    "healthRequirements": "健康告知要求",
    "occupationLimits": "职业限制"
  },
  "coverageAmount": {
    "min": "最低保额",
    "max": "最高保额",
    "rules": "保额规则说明"
  }
}
```

## 缴费信息
```json
{
  "premiumPayment": {
    "paymentMethods": ["趸交", "年交", "月交"],
    "paymentPeriods": ["3年", "5年", "10年", "20年", "30年", "终身"],
    "premiumCalculation": "保费计算方式",
    "discounts": "优惠政策"
  }
}
```

## 适用客户画像
```json
{
  "targetCustomers": {
    "primaryAudience": "主要目标客户群体",
    "demographics": {
      "ageGroup": "年龄段",
      "incomeLevel": "收入水平",
      "familyStatus": "家庭状况"
    },
    "needs": [
      "客户需求1",
      "客户需求2",
      "客户需求3"
    ],
    "scenarios": [
      "适用场景1",
      "适用场景2",
      "适用场景3"
    ]
  }
}
```

## 销售话术要点
```json
{
  "salesPoints": {
    "openingStatement": "开场白模板",
    "needsAnalysis": [
      "需求挖掘问题1",
      "需求挖掘问题2"
    ],
    "productPresentation": {
      "benefits": "利益点介绍",
      "examples": "案例说明",
      "comparison": "竞品对比"
    },
    "objectionHandling": [
      {
        "objection": "常见异议",
        "response": "应对话术"
      }
    ],
    "closingTechniques": [
      "成交技巧1",
      "成交技巧2"
    ]
  }
}
```

## 产品组合建议
```json
{
  "productCombination": {
    "complementaryProducts": [
      "互补产品1",
      "互补产品2"
    ],
    "packageSuggestions": [
      {
        "scenario": "场景描述",
        "products": ["产品1", "产品2"],
        "rationale": "组合理由"
      }
    ]
  }
}
```

## 风险提示
```json
{
  "riskDisclosure": {
    "investmentRisks": "投资风险说明",
    "policyRisks": "保单风险说明",
    "marketRisks": "市场风险说明",
    "liquidityRisks": "流动性风险说明"
  }
}
```

## 常见问题FAQ
```json
{
  "faq": [
    {
      "question": "常见问题1",
      "answer": "详细回答"
    },
    {
      "question": "常见问题2",
      "answer": "详细回答"
    }
  ]
}
```

## 更新记录
```json
{
  "updateHistory": [
    {
      "date": "更新日期",
      "version": "版本号",
      "changes": "更新内容",
      "updatedBy": "更新人"
    }
  ]
}
```

---

## 使用说明

1. **数据完整性**：确保所有必填字段都有准确信息
2. **格式统一**：严格按照JSON格式填写，便于系统解析
3. **内容准确**：所有信息需与官方产品条款一致
4. **定期更新**：产品信息变更时及时更新对应字段
5. **版本控制**：每次更新都要记录在更新记录中

## 输出示例

基于此格式整理的产品信息可以直接用于：
- AI智能推荐系统
- 客户匹配算法
- 销售培训材料
- 产品对比分析
- 客户服务支持

此标准格式确保了产品信息的结构化、标准化和可复用性。