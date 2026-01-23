# 联盟链接管理指南
Affiliate Links Management Guide

---

## 📊 产品总数统计

| 类别 | 数量 | 有链接 | 待添加 |
|------|------|--------|--------|
| **相机 Cameras** | 28 | 24 | 4 |
| **镜头 Lenses** | 13 | 12 | 1 |
| **配件 Accessories** | 9 | 9 | 0 |
| **总计 Total** | **50** | **45** | **5** |

---

## 📍 配置文件位置

**文件路径**: `src/config/affiliateLinks.js`

---

## 🔧 如何维护

### 1. 添加新产品联盟链接

1. 打开 `src/config/affiliateLinks.js`
2. 找到对应的品牌分类区域（如 SONY 索尼相机）
3. 添加新产品条目：

```javascript
'your-product-id': {
    name: '产品名称',
    price: 1999,
    currency: 'USD',
    url: 'https://amzn.to/XXXXXXX',  // 你的联盟链接
},
```

### 2. 更新现有产品链接

搜索产品ID，修改 `url` 字段：

```javascript
'sony-a7c-ii': {
    ...
    url: 'https://amzn.to/新链接',  // 修改这里
},
```

### 3. 获取Amazon联盟链接

1. 登录 Amazon Associates
2. 搜索产品
3. 点击 "Get Link" → "Text" → 复制短链接（amzn.to格式）

---

## 📋 产品ID速查表

### 相机 Cameras (28款)

| 品牌 | 产品ID | 有链接 |
|------|--------|--------|
| **Sony** | `sony-a6700` | ✅ |
| | `sony-a7c-ii` | ✅ |
| | `sony-a7-iv` / `sony-a7iv` | ✅ |
| | `sony-a7-v` | ❌ 预售 |
| | `sony-zv-e10` | ✅ |
| | `sony-zv-e10-ii` | ✅ |
| | `sony-zv-e1` | ✅ |
| | `sony-fx3` | ✅ |
| **Canon** | `canon-eos-r8` | ✅ |
| | `canon-r50` | ✅ |
| | `canon-r100` | ✅ |
| | `canon-r6-ii` | ✅ |
| | `canon-r5-ii` | ❌ 新品 |
| | `canon-r6-iii` | ❌ 新品 |
| **Nikon** | `nikon-z8` | ✅ |
| | `nikon-z6-iii` | ❌ 新品 |
| **Fujifilm** | `fujifilm-x-t5` | ✅ |
| | `fujifilm-x-s20` | ✅ |
| | `fujifilm-x100vi` | ✅ |
| | `fujifilm-x-t50` | ✅ |
| **Panasonic** | `panasonic-s5-ii` | ✅ |
| | `panasonic-s5-iix` | ✅ |
| | `panasonic-g100d` | ✅ |
| **OM System** | `om-system-om-1-ii` | ❌ |
| | `om-system-om-5` | ✅ |
| **Action** | `dji-osmo-pocket-3` | ✅ |
| | `dji-action-5` | ✅ |
| | `gopro-13` | ✅ |
| | `insta360-x4` | ✅ |

### 镜头 Lenses (13款)

| 卡口 | 产品ID | 有链接 |
|------|--------|--------|
| **Sony E** | `sigma-56-14` | ✅ |
| | `tamron-17-70` | ✅ |
| | `sony-35-18` | ✅ |
| | `sony-70-350` | ✅ |
| **Canon RF** | `canon-rf-50` | ✅ |
| | `canon-rfs-18-150` | ✅ |
| | `canon-rf-85` | ✅ |
| | `canon-rf-24-105` | ✅ |
| **Fuji X** | `fuji-xf-16-50` | ✅ |
| | `fuji-xf56-f12` | ✅ |
| | `fuji-xf23-f2` | ❌ |
| | `fuji-xf-33` | ✅ |
| | `sigma-18-50-fuji` | ✅ |

### 配件 Accessories (9款)

| 类别 | 产品ID | 有链接 |
|------|--------|--------|
| **三脚架** | `peak-travel-tripod` | ✅ |
| | `manfrotto-befree` | ✅ |
| | `ulanzi-mt79` | ✅ |
| **相机包** | `peak-everyday-30` | ✅ |
| | `lowepro-protactic` | ✅ |
| | `wandrd-prvke` | ✅ |
| **SD卡** | `sandisk-extreme-pro-256` | ✅ |
| | `sony-tough-v90` | ✅ |
| | `sandisk-extreme-256` | ✅ |

---

## 🚀 在页面中使用

```astro
---
import { getAffiliateLink } from '../../config/affiliateLinks';
const url = getAffiliateLink('sony-a7c-ii');
---

<a href={url} class="btn-buy" rel="sponsored noopener noreferrer" target="_blank">
  Check Price on Amazon →
</a>
```

---

最后更新: 2026-01-23
