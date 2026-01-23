// Affiliate Links Configuration
// 直接在这里修改你的Amazon affiliate链接，所有review页面会自动使用

export const affiliateLinks = {
    // ========== 新增产品 (2026-01-23) ==========
    'nikon-z6-iii': {
        name: 'Nikon Z6 III Camera Body',
        price: 2499,
        currency: 'USD',
        // ⬇️ 在这里添加你的Amazon affiliate链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0D5XXXXX', // 替换为实际ASIN
    },

    'canon-r5-ii': {
        name: 'Canon EOS R5 Mark II Camera Body',
        price: 4299,
        currency: 'USD',
        // ⬇️ 在这里添加你的Amazon affiliate链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0D6XXXXX', // 替换为实际ASIN
    },

    'fujifilm-x-s20': {
        name: 'Fujifilm X-S20 Camera Body',
        price: 1299,
        currency: 'USD',
        // ⬇️ 在这里添加你的Amazon affiliate链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0C5KXXXXX', // 替换为实际ASIN
    },

    'om-system-om-1-ii': {
        name: 'OM System OM-1 Mark II Camera Body',
        price: 2199,
        currency: 'USD',
        // ⬇️ 在这里添加你的Amazon affiliate链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0DXXXXX', // 替换为实际ASIN
    },

    // ========== 现有产品 ==========
    'sony-a7c-ii': {
        name: 'Sony A7C II Camera Body',
        price: 2199,
        currency: 'USD',
        // ⬇️ 替换为你的链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0CL5XXXXX',
    },

    'sony-a7-iv': {
        name: 'Sony A7 IV Camera Body',
        price: 2499,
        currency: 'USD',
        // ⬇️ 替换为你的链接
        url: 'https://www.amazon.com/dp/B09JZT6YK5?tag=你的tag-20',
        asin: 'B09JZT6YK5',
    },

    'canon-eos-r8': {
        name: 'Canon EOS R8 Camera Body',
        price: 1499,
        currency: 'USD',
        // ⬇️ 替换为你的链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0BTY5XXXXX',
    },

    'sony-zv-e10': {
        name: 'Sony ZV-E10 Camera',
        price: 698,
        currency: 'USD',
        // ⬇️ 替换为你的链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B099ZXXXXX',
    },

    'nikon-z8': {
        name: 'Nikon Z8 Camera Body',
        price: 3999,
        currency: 'USD',
        // ⬇️ 替换为你的链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0C4KXXXXX',
    },

    'panasonic-s5-ii': {
        name: 'Panasonic Lumix S5 II Camera Body',
        price: 1999,
        currency: 'USD',
        // ⬇️ 替换为你的链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0BPXXXXX',
    },

    'dji-osmo-pocket-3': {
        name: 'DJI Osmo Pocket 3',
        price: 519,
        currency: 'USD',
        // ⬇️ 替换为你的链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0CLXXXXX',
    },

    'fujifilm-x-t5': {
        name: 'Fujifilm X-T5 Camera Body',
        price: 1699,
        currency: 'USD',
        // ⬇️ 替换为你的链接
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: 'B0BM5XXXXX',
    },

    'sony-a7-v': {
        name: 'Sony A7 V Camera Body',
        price: 3999,
        currency: 'USD',
        // ⬇️ 替换为你的链接 (预售产品)
        url: 'https://www.amazon.com/dp/ASIN?tag=你的tag-20',
        asin: '预售产品-待确认',
    },
};

// Helper function to get affiliate link
export function getAffiliateLink(productId) {
    return affiliateLinks[productId]?.url || '#';
}

// Helper function to get product info
export function getProductInfo(productId) {
    return affiliateLinks[productId] || null;
}
