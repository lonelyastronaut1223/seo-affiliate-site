# Affiliate Links Configuration

## 📝 说明
此文件包含所有产品的Amazon affiliate链接占位符。
每次添加新review或guide时会自动更新此文件。

## 🔗 使用方法
1. 在Amazon Associates后台获取产品链接
2. 将链接添加到对应产品的 `affiliate_url` 字段
3. 确保包含你的associate tag

---

## 最新添加 (2026-01-23)

### Nikon Z6 III
- **Product**: Nikon Z6 III Camera Body
- **Price**: $2,499
- **Review URL**: /reviews/nikon-z6-iii-review
- **Affiliate URL**: `待添加` ⬅️ 添加Amazon链接
- **Amazon ASIN**: B0D5XXXXX (需要查找)
- **Notes**: 24MP partially stacked sensor, 6K video

### Canon EOS R5 Mark II
- **Product**: Canon EOS R5 Mark II Camera Body
- **Price**: $4,299
- **Review URL**: /reviews/canon-r5-ii-review
- **Affiliate URL**: `待添加` ⬅️ 添加Amazon链接
- **Amazon ASIN**: B0D6XXXXX (需要查找)
- **Notes**: 45MP, 8K 60p RAW, Eye Control AF

### Fujifilm X-S20
- **Product**: Fujifilm X-S20 Camera Body
- **Price**: $1,299
- **Review URL**: /reviews/fujifilm-x-s20-review
- **Affiliate URL**: `待添加` ⬅️ 添加Amazon链接
- **Amazon ASIN**: B0C5KXXXXX (需要查找)
- **Notes**: 26MP X-Trans, 6.2K video, IBIS

### OM System OM-1 Mark II
- **Product**: OM System OM-1 Mark II Camera Body
- **Price**: $2,199
- **Review URL**: /reviews/om-system-om-1-ii-review
- **Affiliate URL**: `待添加` ⬅️ 添加Amazon链接
- **Amazon ASIN**: B0DXXXXX (需要查找)
- **Notes**: 20MP MFT, 120fps, IP53 weather sealing

---

## 现有Products

### Sony A7C II
- **Product**: Sony A7C II Camera Body
- **Price**: $2,199
- **Review URL**: /reviews/sony-a7c-ii-review
- **Affiliate URL**: `https://amzn.to/xxxxx` ⬅️ 更新你的链接
- **Amazon ASIN**: B0CL5XXXXX

### Sony A7 IV
- **Product**: Sony A7 IV Camera Body
- **Price**: $2,499
- **Review URL**: /reviews/sony-a7-iv-review
- **Affiliate URL**: `https://amzn.to/xxxxx` ⬅️ 更新你的链接
- **Amazon ASIN**: B09JZT6YK5

### Canon EOS R8
- **Product**: Canon EOS R8 Camera Body
- **Price**: $1,499
- **Review URL**: /reviews/canon-eos-r8-review
- **Affiliate URL**: `https://amzn.to/xxxxx` ⬅️ 更新你的链接
- **Amazon ASIN**: B0BTY5XXXXX

### Sony ZV-E10
- **Product**: Sony ZV-E10 Camera
- **Price**: $698
- **Review URL**: /reviews/sony-zv-e10-review
- **Affiliate URL**: `https://amzn.to/xxxxx` ⬅️ 更新你的链接
- **Amazon ASIN**: B099ZXXXXX

### Nikon Z8
- **Product**: Nikon Z8 Camera Body
- **Price**: $3,999
- **Review URL**: /reviews/nikon-z8-review
- **Affiliate URL**: `https://amzn.to/xxxxx` ⬅️ 更新你的链接
- **Amazon ASIN**: B0C4KXXXXX

### Panasonic Lumix S5 II
- **Product**: Panasonic Lumix S5 II Camera Body
- **Price**: $1,999
- **Review URL**: /reviews/panasonic-s5-ii-review
- **Affiliate URL**: `https://amzn.to/xxxxx` ⬅️ 更新你的链接
- **Amazon ASIN**: B0BPXXXXX

### DJI Osmo Pocket 3
- **Product**: DJI Osmo Pocket 3
- **Price**: $519
- **Review URL**: /reviews/dji-osmo-pocket-3-review
- **Affiliate URL**: `https://amzn.to/xxxxx` ⬅️ 更新你的链接
- **Amazon ASIN**: B0CLXXXXX

### Fujifilm X-T5
- **Product**: Fujifilm X-T5 Camera Body
- **Price**: $1,699
- **Review URL**: /reviews/fujifilm-x-t5-review
- **Affiliate URL**: `https://amzn.to/xxxxx` ⬅️ 更新你的链接
- **Amazon ASIN**: B0BM5XXXXX

### Sony A7 V
- **Product**: Sony A7 V Camera Body
- **Price**: $3,999
- **Review URL**: /reviews/sony-a7-v-review
- **Affiliate URL**: `待添加` ⬅️ 添加Amazon链接
- **Amazon ASIN**: 预售产品，待确认
- **Notes**: 61MP, 8K 30p

---

## 📋 Affiliate Link替换指南

### 在Review页面中替换
找到每个review中的 "Check Price on Amazon" 按钮：

```astro
<a
  href="#"  ⬅️ 将 # 替换为上面的 Affiliate URL
  class="btn-buy"
  rel="sponsored noopener noreferrer"
  target="_blank"
>
  Check Price on Amazon &rarr;
</a>
```

### 替换文件列表
- `/src/pages/reviews/nikon-z6-iii-review.astro`
- `/src/pages/reviews/canon-r5-ii-review.astro`
- `/src/pages/reviews/fujifilm-x-s20-review.astro`
- `/src/pages/reviews/om-system-om-1-ii-review.astro`

### 批量替换命令 (可选)
```bash
# 示例：替换Nikon Z6 III的链接
sed -i '' 's|href="#"|href="https://amzn.to/YOUR_LINK_HERE"|' src/pages/reviews/nikon-z6-iii-review.astro
```

---

## 🎯 下次添加新产品时的流程

1. 创建新review文件
2. **立即更新此文件**，添加新产品信息
3. 获取Amazon affiliate链接
4. 更新review文件中的 `href="#"` 为实际链接
5. Commit时在commit message中提醒更新affiliate links

---

## 📊 待添加的未来Products

根据implementation_plan.md，以下产品将在未来几天添加：

### 即将添加 (需要准备affiliate links)
- [ ] Best Cameras for YouTube Guide - 多个产品
- [ ] Best Low-Light Cameras Guide - 多个产品
- [ ] Best Wildlife Cameras Guide - 多个产品

每个Guide通常包含5-8个产品推荐，每个都需要affiliate link。

---

**最后更新**: 2026-01-23
**下次更新**: Day 2 (DE translations) - 不需要新links
**下次需要新links**: Day 4 (YouTube Guide)
