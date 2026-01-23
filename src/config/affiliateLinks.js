/**
 * Centralized Affiliate Links Configuration
 * 集中管理所有Amazon联盟链接
 * 
 * 使用方法:
 * import { getAffiliateLink } from '../../config/affiliateLinks';
 * const url = getAffiliateLink('sony-a7c-ii');
 * 
 * 添加新产品:
 * 1. 在下面添加新的产品条目
 * 2. 填写产品名称、价格、Amazon链接和ASIN
 * 3. 在review页面中导入并使用getAffiliateLink()函数
 */

export const affiliateLinks = {
    // ========== SONY 索尼相机 ==========
    'sony-a6700': {
        name: 'Sony A6700',
        price: 1398,
        currency: 'USD',
        url: 'https://amzn.to/3NpavhW',
        asin: 'B0C7KXXXXX',
    },

    'sony-a7c-ii': {
        name: 'Sony A7C II Camera Body',
        price: 2199,
        currency: 'USD',
        url: 'https://amzn.to/49XHouC',
        asin: 'B0CL5XXXXX',
    },

    'sony-a7-iv': {
        name: 'Sony A7 IV Camera Body',
        price: 2499,
        currency: 'USD',
        url: 'https://amzn.to/3Zmgs1u',
        asin: 'B09JZT6YK5',
    },

    'sony-a7-v': {
        name: 'Sony A7 V Camera Body',
        price: 3999,
        currency: 'USD',
        url: '', // 预售产品，暂未上市
        asin: '待确认',
    },

    'sony-zv-e10': {
        name: 'Sony ZV-E10 Camera',
        price: 698,
        currency: 'USD',
        url: 'https://amzn.to/3NqCxth',
        asin: 'B099ZXXXXX',
    },

    'sony-zv-e10-ii': {
        name: 'Sony ZV-E10 II',
        price: 998,
        currency: 'USD',
        url: 'https://amzn.to/49HqAH3',
        asin: 'B0D1XXXXX',
    },

    'sony-zv-e1': {
        name: 'Sony ZV-E1',
        price: 2198,
        currency: 'USD',
        url: 'https://amzn.to/3Le0oMc',
        asin: 'B0BXXXXX',
    },

    'sony-fx3': {
        name: 'Sony FX3',
        price: 3898,
        currency: 'USD',
        url: 'https://amzn.to/4b0w6Ha',
        asin: 'B08XXXXX',
    },

    // ========== CANON 佳能相机 ==========
    'canon-eos-r8': {
        name: 'Canon EOS R8 Camera Body',
        price: 1499,
        currency: 'USD',
        url: 'https://amzn.to/3Lvm06M',
        asin: 'B0BTY5XXXXX',
    },

    'canon-r50': {
        name: 'Canon EOS R50',
        price: 679,
        currency: 'USD',
        url: 'https://amzn.to/3YBJTwt',
        asin: 'B0BXXXXX',
    },

    'canon-r100': {
        name: 'Canon EOS R100',
        price: 479,
        currency: 'USD',
        url: 'https://amzn.to/45FQ6eA',
        asin: 'B0CXXXXX',
    },

    'canon-r6-ii': {
        name: 'Canon EOS R6 Mark II',
        price: 2499,
        currency: 'USD',
        url: 'https://amzn.to/4sHWE6q',
        asin: 'B0BXXXXX',
    },

    'canon-r5-ii': {
        name: 'Canon EOS R5 Mark II Camera Body',
        price: 4299,
        currency: 'USD',
        url: '', // 新品，暂无联盟链接
        asin: 'B0D6XXXXX',
    },

    // ========== NIKON 尼康相机 ==========
    'nikon-z8': {
        name: 'Nikon Z8 Camera Body',
        price: 3999,
        currency: 'USD',
        url: 'https://amzn.to/4sMa95c',
        asin: 'B0C4KXXXXX',
    },

    'nikon-z6-iii': {
        name: 'Nikon Z6 III Camera Body',
        price: 2499,
        currency: 'USD',
        url: '', // 待添加
        asin: 'B0D5XXXXX',
    },

    // ========== FUJIFILM 富士相机 ==========
    'fujifilm-x-t5': {
        name: 'Fujifilm X-T5 Camera Body',
        price: 1699,
        currency: 'USD',
        url: 'https://amzn.to/4qSEPQj',
        asin: 'B0BM5XXXXX',
    },

    'fujifilm-x-s20': {
        name: 'Fujifilm X-S20 Camera Body',
        price: 1299,
        currency: 'USD',
        url: 'https://amzn.to/3YJrfTj',
        asin: 'B0C5KXXXXX',
    },

    'fujifilm-x100vi': {
        name: 'Fujifilm X100VI',
        price: 1599,
        currency: 'USD',
        url: 'https://amzn.to/4pGFIdE',
        asin: 'B0CXXXXX',
    },

    'fujifilm-x-t50': {
        name: 'Fujifilm X-T50',
        price: 1399,
        currency: 'USD',
        url: 'https://amzn.to/4pJH5se',
        asin: 'B0DXXXXX',
    },

    // ========== PANASONIC 松下相机 ==========
    'panasonic-s5-ii': {
        name: 'Panasonic Lumix S5 II Camera Body',
        price: 1999,
        currency: 'USD',
        url: 'https://amzn.to/45FQbyU',
        asin: 'B0BPXXXXX',
    },

    'panasonic-s5-iix': {
        name: 'Panasonic Lumix S5 IIX',
        price: 2197,
        currency: 'USD',
        url: 'https://amzn.to/49nmk0t',
        asin: 'B0BXXXXX',
    },

    'panasonic-g100d': {
        name: 'Panasonic Lumix G100D',
        price: 747,
        currency: 'USD',
        url: 'https://amzn.to/4sHwgtm',
        asin: 'B0CXXXXX',
    },

    // ========== OM SYSTEM 奥林巴斯 ==========
    'om-system-om-1-ii': {
        name: 'OM System OM-1 Mark II Camera Body',
        price: 2199,
        currency: 'USD',
        url: '', // 待添加
        asin: 'B0DXXXXX',
    },

    'om-system-om-5': {
        name: 'OM System OM-5',
        price: 1199,
        currency: 'USD',
        url: 'https://amzn.to/49TF1cd',
        asin: 'B0BXXXXX',
    },

    // ========== DJI & ACTION CAMERAS 运动相机 ==========
    'dji-osmo-pocket-3': {
        name: 'DJI Osmo Pocket 3',
        price: 519,
        currency: 'USD',
        url: 'https://amzn.to/3NlCOOg',
        asin: 'B0CLXXXXX',
    },

    'dji-action-5': {
        name: 'DJI Action 5 Pro',
        price: 349,
        currency: 'USD',
        url: 'https://amzn.to/4jHiYc3',
        asin: 'B0DXXXXX',
    },

    'gopro-13': {
        name: 'GoPro Hero 13 Black',
        price: 399,
        currency: 'USD',
        url: 'https://amzn.to/3Ne6SLE',
        asin: 'B0DXXXXX',
    },

    'insta360-x4': {
        name: 'Insta360 X4',
        price: 499,
        currency: 'USD',
        url: 'https://amzn.to/4aUs0jM',
        asin: 'B0CXXXXX',
    },

    // ========== ACCESSORIES 配件 ==========
    'sandisk-extreme-pro-256gb': {
        name: 'SanDisk Extreme Pro 256GB SD Card',
        price: 39,
        currency: 'USD',
        url: 'https://amzn.to/4sPSPMl',
        asin: 'B09X7XXXXX',
    },
};

/**
 * 获取产品的Amazon联盟链接
 * @param {string} productId - 产品ID（如 'sony-a7c-ii'）
 * @returns {string} Amazon联盟链接，如果未找到返回 '#'
 */
export function getAffiliateLink(productId) {
    return affiliateLinks[productId]?.url || '#';
}

/**
 * 获取产品完整信息
 * @param {string} productId - 产品ID
 * @returns {object|null} 产品信息对象，如果未找到返回 null
 */
export function getProductInfo(productId) {
    return affiliateLinks[productId] || null;
}
