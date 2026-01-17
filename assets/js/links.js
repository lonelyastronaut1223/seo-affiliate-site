// Affiliate Link Configuration
const affiliateLinks = {
    // Sony
    "sony-a6700": "https://amzn.to/3NpavhW",
    "sony-a7c-ii": "https://amzn.to/49XHouC",
    "sony-a7iv": "https://amzn.to/3Zmgs1u",
    "sony-zv-e10-ii": "https://amzn.to/49HqAH3",
    "sony-zv-e10": "https://amzn.to/3NqCxth",
    "sony-zv-e1": "https://amzn.to/3Le0oMc",
    "sony-fx3": "https://amzn.to/4b0w6Ha",

    // Fujifilm
    "fuji-x100vi": "https://amzn.to/4pGFIdE",
    "fuji-x-t50": "https://amzn.to/4pJH5se",
    "fuji-x-t5": "https://amzn.to/4qSEPQj",
    "fuji-xt5": "https://amzn.to/4qT3Laf", // Alternative key
    "fuji-x-s20": "https://amzn.to/3YJrfTj",
    "fuji-xs10": "", // Used only, no new link

    // Canon
    "canon-r50": "https://amzn.to/3YBJTwt",
    "canon-r100": "https://amzn.to/45FQ6eA",
    "canon-r8": "https://amzn.to/3Lvm06M",
    "canon-r6ii": "https://amzn.to/4sHWE6q",
    "canon-r6-ii": "https://amzn.to/4sHWE6q", // Alternative key

    // Panasonic
    "panasonic-s5ii": "https://amzn.to/45FQbyU",
    "panasonic-s5iix": "https://amzn.to/49nmk0t",
    "lumix-g100d": "https://amzn.to/4sHwgtm", // HTML ID is lumix-g100d

    // Nikon
    "nikon-z8": "https://amzn.to/4sMa95c",

    // OM System
    "om-system-om5": "https://amzn.to/49TF1cd",

    // DJI & GoPro
    "dji-pocket-3": "https://amzn.to/3NlCOOg",
    "dji-action-5": "https://amzn.to/4jHiYc3", // HTML ID is dji-action-5
    "gopro-13": "https://amzn.to/3Ne6SLE", // HTML ID is gopro-13
    "insta360-x4": "https://amzn.to/4aUs0jM",

    // Comparison Specific - New products not yet on Amazon
    "sony-a7-v": "", // Not available yet
    "canon-r6-iii": "" // Not available yet
};

// Main function to apply links
function applyAffiliateLinks() {
    console.log("Applying affiliate links...");
    let updatedCount = 0;

    // Check language
    const isGerman = document.documentElement.lang === 'de';
    const checkPriceText = isGerman ? 'Preis prüfen' : 'Check Price';

    // Helper to apply attributes
    const updateBtn = (btn, url) => {
        if (btn) {
            btn.href = url;
            btn.target = "_blank";
            btn.rel = "sponsored noopener noreferrer";
        }
    };

    for (const [id, link] of Object.entries(affiliateLinks)) {
        if (!link || link === "#" || link === "") continue;

        // 1. Main Buy Buttons (Strategy A: Wrapper ID)
        const section = document.getElementById(id);
        if (section) {
            const btn = section.querySelector('.btn-buy');
            updateBtn(btn, link);
        }

        // 2. Main Buy Buttons (Strategy B: Direct Data Attribute - More Robust)
        const dataButtons = document.querySelectorAll(`.btn-buy[data-product="${id}"]`);
        dataButtons.forEach(btn => updateBtn(btn, link));

        // 3. Comparison Tables
        const selector = `a[href="#${id}"]`;
        const internalAnchors = document.querySelectorAll(selector);

        internalAnchors.forEach(anchor => {
            const row = anchor.closest('tr');
            if (row) {
                const priceCell = row.querySelector('.price-check');
                if (priceCell) {
                    // Distinct visual style (Green) to confirm activation
                    priceCell.innerHTML = `
                        <a href="${link}" target="_blank" rel="sponsored noopener noreferrer" 
                           style="color: #10b981; text-decoration: none; font-weight: 800; display: inline-flex; align-items: center; gap: 4px;">
                           ${checkPriceText} <span style="font-size: 1.2em;">&rarr;</span>
                        </a>
                    `;
                    updatedCount++;
                }
            }
        });
    }
    console.log(`Links applied. Updated ${updatedCount} comparisons/buttons.`);
}

// Run immediately if DOM is ready, otherwise wait
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyAffiliateLinks);
} else {
    applyAffiliateLinks();
}
