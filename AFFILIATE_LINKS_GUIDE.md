# 联盟链接管理系统使用说明
Affiliate Links Management Guide

---

## 📍 系统概述

### 当前系统架构

**配置文件**: `src/config/affiliateLinks.js`  
**功能**: 集中管理所有Amazon联盟链接

### 历史迁移
- ❌ **旧系统**: `assets/js/links.js` (前端JavaScript动态注入) - 已废弃
- ✅ **新系统**: `src/config/affiliateLinks.js` (Astro编译时注入) - 当前使用

---

## 🔗 当前可用的联盟链接

### Sony 索尼
- `sony-a6700`: https://amzn.to/3NpavhW
- `sony-a7c-ii`: https://amzn.to/49XHouC
- `sony-a7-iv`: https://amzn.to/3Zmgs1u
- `sony-zv-e10`: https://amzn.to/3NqCxth
- `sony-zv-e10-ii`: https://amzn.to/49HqAH3
- `sony-zv-e1`: https://amzn.to/3Le0oMc
- `sony-fx3`: https://amzn.to/4b0w6Ha

### Canon 佳能
- `canon-eos-r8`: https://amzn.to/3Lvm06M
- `canon-r50`: https://amzn.to/3YBJTwt
- `canon-r100`: https://amzn.to/45FQ6eA
- `canon-r6-ii`: https://amzn.to/4sHWE6q

### Nikon 尼康
- `nikon-z8`: https://amzn.to/4sMa95c

### Fujifilm 富士
- `fujifilm-x-t5`: https://amzn.to/4qSEPQj
- `fujifilm-x-s20`: https://amzn.to/3YJrfTj
- `fujifilm-x100vi`: https://amzn.to/4pGFIdE
- `fujifilm-x-t50`: https://amzn.to/4pJH5se

### Panasonic 松下
- `panasonic-s5-ii`: https://amzn.to/45FQbyU
- `panasonic-s5-iix`: https://amzn.to/49nmk0t
- `panasonic-g100d`: https://amzn.to/4sHwgtm

### OM System 奥林巴斯
- `om-system-om-5`: https://amzn.to/49TF1cd

### DJI & Action Cameras 运动相机
- `dji-osmo-pocket-3`: https://amzn.to/3NlCOOg
- `dji-action-5`: https://amzn.to/4jHiYc3
- `gopro-13`: https://amzn.to/3Ne6SLE
- `insta360-x4`: https://amzn.to/4aUs0jM

### Accessories 配件
- `sandisk-extreme-pro-256gb`: https://amzn.to/4sPSPMl

### 🚧 待添加链接的产品
以下产品在配置文件中已定义，但联盟链接为空（需要后续添加）：
- `sony-a7-v` (预售产品)
- `canon-r5-ii` (新品)
- `nikon-z6-iii` (待添加)
- `om-system-om-1-ii` (待添加)

---

## 📖 使用方法

### 1. 在新的评论页面中使用

```astro
---
import BaseLayout from '../../layouts/BaseLayout.astro';
import { getAffiliateLink } from '../../config/affiliateLinks';

// 获取联盟链接
const affiliateUrl = getAffiliateLink('sony-a7c-ii');
---

<BaseLayout title="Sony A7C II Review" description="...">
  <a href={affiliateUrl} 
     class="btn-buy" 
     rel="sponsored noopener noreferrer" 
     target="_blank">
    Check Price on Amazon &rarr;
  </a>
</BaseLayout>
```

### 2. 添加新产品联盟链接

在 `src/config/affiliateLinks.js` 中添加：

```javascript
export const affiliateLinks = {
    // ... 现有产品 ...

    'your-new-product': {
        name: 'Product Full Name',
        price: 1999,
        currency: 'USD',
        url: 'https://amzn.to/XXXXXXX',  // ✅ 在这里填入你的Amazon联盟链接
        asin: 'B0XXXXXXX',  // Amazon产品ASIN码
    },
};
```

### 3. 查找Amazon ASIN码

1. 访问Amazon产品页面
2. 在URL中查找ASIN码：
   - URL格式：`amazon.com/dp/B09JZT6YK5`
   - ASIN = `B09JZT6YK5`

---

## ⚠️ 当前状态和待办事项

### ❌ 当前问题
**所有评论页面仍在使用占位符 `href="#"`，没有连接到配置文件！**

### ✅ 已完成
- [x] 创建集中配置文件 `src/config/affiliateLinks.js`
- [x] 从旧的 `assets/js/links.js` 提取所有真实联盟链接
- [x] 整合所有链接到新配置文件

### 🔧 待完成 (下一步)
- [ ] 修改所有评论页面，将硬编码的 `href="#"` 替换为 `getAffiliateLink()` 动态调用
- [ ] 为新产品（Nikon Z6 III, Canon R5 II, Fujifilm X-S20, OM-1 II）添加真实联盟链接
- [ ] 测试所有页面的联盟链接是否正常工作

---

## 🎯 集成示例

### 修改前（硬编码占位符）
```astro
<a href="#" class="btn-buy" rel="sponsored noopener noreferrer" target="_blank">
  Check Price on Amazon &rarr;
</a>
```

### 修改后（动态从配置获取）
```astro
---
import { getAffiliateLink } from '../../config/affiliateLinks';
const productId = 'sony-a7c-ii';
const affiliateUrl = getAffiliateLink(productId);
---

<a href={affiliateUrl} class="btn-buy" rel="sponsored noopener noreferrer" target="_blank">
  Check Price on Amazon &rarr;
</a>
```

---

## 📝 维护注意事项

1. **所有联盟链接统一在 `src/config/affiliateLinks.js` 中管理**
2. **添加新产品时，记得同时添加英文和德语页面的链接**
3. **空链接会返回 `#`，不会破坏页面**
4. **确保所有链接包含 `rel="sponsored noopener noreferrer"` 属性**

---

## 🛠️ 技术细节

### 辅助函数

#### `getAffiliateLink(productId)`
返回指定产品的Amazon联盟链接URL

**参数**: 
- `productId` (string): 产品ID，如 `'sony-a7c-ii'`

**返回值**: 
- (string): Amazon联盟链接URL，如果未找到返回 `'#'`

**示例**:
```javascript
getAffiliateLink('sony-a7c-ii')  // 返回: 'https://amzn.to/49XHouC'
getAffiliateLink('invalid-id')   // 返回: '#'
```

#### `getProductInfo(productId)`
返回指定产品的完整信息对象

**参数**: 
- `productId` (string): 产品ID

**返回值**: 
- (object|null): 包含 name, price, currency, url, asin 的对象，如果未找到返回 `null`

**示例**:
```javascript
getProductInfo('sony-a7c-ii')
// 返回: { name: 'Sony A7C II Camera Body', price: 2199, currency: 'USD', url: '...', asin: '...' }
```

---

最后更新: 2026-01-23
