#!/usr/bin/env node
/**
 * sync_links.js
 * Automatically synchronizes affiliate links from src/config/affiliateLinks.js 
 * to public/assets/js/links.js to maintain consistency.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '../../');

const SOURCE_FILE = path.join(ROOT_DIR, 'src/config/affiliateLinks.js');
const TARGET_FILE = path.join(ROOT_DIR, 'public/assets/js/links.js');

console.log('🔗 Starting Affiliate Link Sync...');

try {
    // 1. Read source configuration
    const sourceContent = fs.readFileSync(SOURCE_FILE, 'utf8');

    // 2. Extract the affiliateLinks object using regex
    // This expects the export const affiliateLinks = { ... }; pattern
    const match = sourceContent.match(/export const affiliateLinks = (\{[\s\S]*?\});/);

    if (!match) {
        throw new Error('Could not find affiliateLinks object in source file.');
    }

    // We want to transform the complex object { name, price, url } into a simple mapping { id: url }
    // Since we are running in Node and the source is ESM, we can't easily import it without setup
    // But we can parse the string or evaluate it in a sandbox if needed.
    // For simplicity and safety, let's use a regex-based extraction of key/url pairs.

    const rawObject = match[1];
    const linkMap = {};

    // Pattern to find 'key': { ... url: '...' }
    // Using a more robust regex to handle nested structures
    const entryRegex = /'([^']+)':\s*\{[\s\S]*?url:\s*'([^']*)'/g;
    let entryMatch;

    while ((entryMatch = entryRegex.exec(rawObject)) !== null) {
        const [_, id, url] = entryMatch;
        if (url) {
            linkMap[id] = url;
        }
    }

    // 3. Generate the target public/assets/js/links.js content
    let targetContent = `
/**
 * AUTO-GENERATED FILE - DO NOT MODIFY DIRECTLY
 * This file is generated from src/config/affiliateLinks.js by scripts/core/sync_links.js
 * Last Updated: ${new Date().toISOString()}
 */

const affiliateLinks = ${JSON.stringify(linkMap, null, 4)};

function applyAffiliateLinks() {
    const isGerman = document.documentElement.lang === 'de';
    const checkPriceText = isGerman ? 'Preis prüfen' : 'Check Price';

    const updateBtn = (btn, url) => {
        if (btn && url && url !== "NEED_LINK" && url !== "#") {
            btn.href = url;
            btn.target = "_blank";
            btn.rel = "sponsored noopener noreferrer";
        }
    };

    for (const [id, link] of Object.entries(affiliateLinks)) {
        if (!link || link === "#" || link === "" || link === "NEED_LINK") continue;

        // Strategy A: Wrapper ID
        const section = document.getElementById(id);
        if (section) {
            const btn = section.querySelector('.btn-buy');
            updateBtn(btn, link);
        }

        // Strategy B: Data attribute
        document.querySelectorAll(\`.btn-buy[data-product="\${id}"]\`).forEach(btn => updateBtn(btn, link));

        // Strategy C: Comparison tables
        document.querySelectorAll(\`a[href="#\${id}"]\`).forEach(anchor => {
            const row = anchor.closest('tr');
            if (row) {
                const priceCell = row.querySelector('.price-check');
                if (priceCell) {
                    priceCell.innerHTML = \`<a href="\${link}" target="_blank" rel="sponsored noopener noreferrer" style="color:#10b981;text-decoration:none;font-weight:800;display:inline-flex;align-items:center;gap:4px">\${checkPriceText} <span style="font-size:1.2em">&rarr;</span></a>\`;
                }
            }
        });
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyAffiliateLinks);
} else {
    applyAffiliateLinks();
}
`;

    fs.writeFileSync(TARGET_FILE, targetContent.trim() + '\n');
    console.log(`✅ Successfully synced ${Object.keys(linkMap).length} links to ${path.relative(ROOT_DIR, TARGET_FILE)}`);

} catch (error) {
    console.error('❌ Sync failed:', error.message);
    process.exit(1);
}
