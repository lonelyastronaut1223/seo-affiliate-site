/**
 * ═══════════════════════════════════════════════════════════════════════════
 *                      Deals 配置文件 - Deals Configuration
 * ═══════════════════════════════════════════════════════════════════════════
 * 
 * 📅 最后更新 / Last Updated: 2026-01-30
 * 📊 当前 Deals 数量 / Active Deals: 5
 * 
 * ═══════════════════════════════════════════════════════════════════════════
 */

export const dealsConfig = {
    lastUpdated: '2026-01-30',

    // Active deals
    deals: [
        // ═══════════════════════════════════════════════════════════════════════
        //                           🔥 HOT DEALS
        // ═══════════════════════════════════════════════════════════════════════
        {
            id: 'sony-zv-e10-deal',
            name: 'Sony ZV-E10',
            category: 'camera',
            originalPrice: 798,
            dealPrice: 698,
            currency: 'USD',
            currencySymbol: '$',
            savingsAmount: 100,
            savingsPercent: 13,
            description: 'The best budget vlog camera just dropped in price. Includes 16-50mm lens.',
            amazonUrl: 'https://amzn.to/49HqAH3',
            expiresAt: null, // null = ongoing deal
            isHot: true,
            isLowest: false,
            isNew: false,
            reviewUrl: '/reviews/sony-zv-e10-review'
        },
        {
            id: 'panasonic-s5-ii-deal',
            name: 'Panasonic S5 II',
            category: 'camera',
            originalPrice: 1999,
            dealPrice: 1748,
            currency: 'USD',
            currencySymbol: '$',
            savingsAmount: 251,
            savingsPercent: 13,
            description: 'Full-frame powerhouse with phase detect AF. Great value for hybrids.',
            amazonUrl: 'https://amzn.to/45FQbyU',
            expiresAt: null,
            isHot: false,
            isLowest: false,
            isNew: false,
            reviewUrl: '/reviews/panasonic-s5-ii-review'
        },
        {
            id: 'sandisk-extreme-pro-256-deal',
            name: 'SanDisk Extreme Pro 256GB',
            category: 'accessory',
            originalPrice: 45,
            dealPrice: 30,
            currency: 'USD',
            currencySymbol: '$',
            savingsAmount: 15,
            savingsPercent: 34,
            description: 'Essential for 4K video. Reliable V30 speed class.',
            amazonUrl: 'https://amzn.to/4sPSPMl',
            expiresAt: null,
            isHot: false,
            isLowest: false,
            isNew: false,
            reviewUrl: null
        },
        {
            id: 'dji-pocket-3-deal',
            name: 'DJI Osmo Pocket 3',
            category: 'camera',
            originalPrice: 520,
            dealPrice: 479,
            currency: 'USD',
            currencySymbol: '$',
            savingsAmount: 41,
            savingsPercent: 8,
            description: 'Creator Combo with wireless mic. Best portable vlog camera. Now 8% off!',
            amazonUrl: 'https://amzn.to/3PmNfHq',
            expiresAt: '2026-02-14',
            isHot: true,
            isLowest: true,
            isNew: true,
            reviewUrl: '/reviews/dji-osmo-pocket-3-review'
        },
        {
            id: 'sony-a6700-deal',
            name: 'Sony A6700',
            category: 'camera',
            originalPrice: 1398,
            dealPrice: 1298,
            currency: 'USD',
            currencySymbol: '$',
            savingsAmount: 100,
            savingsPercent: 7,
            description: 'Best APS-C hybrid with AI autofocus. Great for photo and video.',
            amazonUrl: 'https://amzn.to/3Wx8fTk',
            expiresAt: null,
            isHot: false,
            isLowest: false,
            isNew: false,
            reviewUrl: '/reviews/sony-a6700-review'
        }
    ],

    // German (DE) price conversions (approximate EUR)
    deDeals: [
        {
            id: 'sony-zv-e10-deal',
            name: 'Sony ZV-E10',
            category: 'camera',
            originalPrice: 749,
            dealPrice: 649,
            currency: 'EUR',
            currencySymbol: '€',
            savingsAmount: 100,
            savingsPercent: 13,
            description: 'Die beste Budget-Vlog-Kamera zum Tiefpreis. Inkl. 16-50mm Objektiv.',
            amazonUrl: 'https://amzn.to/49HqAH3',
            expiresAt: null,
            isHot: true,
            isLowest: false,
            isNew: false,
            reviewUrl: '/de/reviews/sony-zv-e10-test'
        },
        {
            id: 'panasonic-s5-ii-deal',
            name: 'Panasonic S5 II',
            category: 'camera',
            originalPrice: 1899,
            dealPrice: 1649,
            currency: 'EUR',
            currencySymbol: '€',
            savingsAmount: 250,
            savingsPercent: 13,
            description: 'Vollformat-Kraftpaket mit Phasen-AF. Gutes Preis-Leistungs-Verhältnis.',
            amazonUrl: 'https://amzn.to/45FQbyU',
            expiresAt: null,
            isHot: false,
            isLowest: false,
            isNew: false,
            reviewUrl: '/de/reviews/panasonic-s5-ii-test'
        },
        {
            id: 'sandisk-extreme-pro-256-deal',
            name: 'SanDisk Extreme Pro 256GB',
            category: 'accessory',
            originalPrice: 42,
            dealPrice: 28,
            currency: 'EUR',
            currencySymbol: '€',
            savingsAmount: 14,
            savingsPercent: 33,
            description: 'Unerlässlich für 4K-Video. Zuverlässige V30-Geschwindigkeitsklasse.',
            amazonUrl: 'https://amzn.to/4sPSPMl',
            expiresAt: null,
            isHot: false,
            isLowest: false,
            isNew: false,
            reviewUrl: null
        },
        {
            id: 'dji-pocket-3-deal',
            name: 'DJI Osmo Pocket 3',
            category: 'camera',
            originalPrice: 490,
            dealPrice: 449,
            currency: 'EUR',
            currencySymbol: '€',
            savingsAmount: 41,
            savingsPercent: 8,
            description: 'Creator Combo mit kabellosen Mikrofon. Beste portable Vlog-Kamera. Jetzt 8% Rabatt!',
            amazonUrl: 'https://amzn.to/3PmNfHq',
            expiresAt: '2026-02-14',
            isHot: true,
            isLowest: true,
            isNew: true,
            reviewUrl: '/de/reviews/dji-osmo-pocket-3-test'
        },
        {
            id: 'sony-a6700-deal',
            name: 'Sony A6700',
            category: 'camera',
            originalPrice: 1299,
            dealPrice: 1199,
            currency: 'EUR',
            currencySymbol: '€',
            savingsAmount: 100,
            savingsPercent: 8,
            description: 'Beste APS-C-Hybrid mit KI-Autofokus. Ideal für Foto und Video.',
            amazonUrl: 'https://amzn.to/3Wx8fTk',
            expiresAt: null,
            isHot: false,
            isLowest: false,
            isNew: false,
            reviewUrl: '/de/reviews/sony-a6700-test'
        }
    ]
};

/**
 * Get active deals (not expired)
 */
export function getActiveDeals(locale = 'en') {
    const deals = locale === 'de' ? dealsConfig.deDeals : dealsConfig.deals;
    const now = new Date();

    return deals.filter(deal => {
        if (!deal.expiresAt) return true;
        return new Date(deal.expiresAt) > now;
    });
}

/**
 * Get deals by category
 */
export function getDealsByCategory(category, locale = 'en') {
    return getActiveDeals(locale).filter(deal => deal.category === category);
}

/**
 * Get hot deals (featured)
 */
export function getHotDeals(locale = 'en') {
    return getActiveDeals(locale).filter(deal => deal.isHot);
}

/**
 * Get last updated date
 */
export function getLastUpdated() {
    return dealsConfig.lastUpdated;
}

/**
 * Calculate days until expiration
 */
export function getDaysUntilExpiration(expiresAt) {
    if (!expiresAt) return null;
    const now = new Date();
    const expires = new Date(expiresAt);
    const diff = expires - now;
    return Math.ceil(diff / (1000 * 60 * 60 * 24));
}

export default dealsConfig;
