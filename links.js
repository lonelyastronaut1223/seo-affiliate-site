// Affiliate Link Configuration
const affiliateLinks = {
    // Sony
    "sony-a6700": "https://amzn.to/49q42vK",
    "sony-zv-e10-ii": "https://amzn.to/49HqAH3",
    "sony-zv-e10": "https://amzn.to/49HqAH3", // Alias for Budget Guide (assuming II link)
    "sony-zv-e1": "https://amzn.to/3Le0oMc",
    "sony-a7iv": "https://amzn.to/4qMgpYK", // HTML ID is sony-a7iv
    "sony-fx3": "https://amzn.to/4b0w6Ha",

    // Fujifilm
    "fuji-x100vi": "https://amzn.to/4pGFIdE",
    "fuji-x-t50": "https://amzn.to/4pJH5se",
    "fuji-x-t5": "https://amzn.to/4qSEPQj",

    // Canon
    "canon-r50": "https://amzn.to/3YBJTwt",
    "canon-r100": "https://amzn.to/45FQ6eA",
    "canon-r8": "https://amzn.to/3Lvm06M",
    "canon-r6ii": "https://amzn.to/4sHWE6q", // HTML ID is canon-r6ii

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

    // Comparison Specific (New)
    "sony-a7-v": "https://amzn.to/4qMgpYK", // Placeholder (using A7 IV link)
    "canon-r6-iii": "https://amzn.to/4sHWE6q", // Placeholder (using R6 II link)
    "canon-r6-ii": "https://amzn.to/4sHWE6q",
    "fuji-x-s20": "https://amzn.to/4pJH5se", // Placeholder (using X-T50 link)
    "sony-a6700": "https://amzn.to/49q42vK" // Ensure explicit key exists
};

// Main function to apply links
function applyAffiliateLinks() {
    console.log("Applying affiliate links...");
    let updatedCount = 0;

    for (const [id, link] of Object.entries(affiliateLinks)) {
        if (!link || link === "#" || link === "") continue;

        // 1. Main Buy Buttons
        const section = document.getElementById(id);
        if (section) {
            const btn = section.querySelector('.btn-buy');
            if (btn) {
                btn.href = link;
                btn.target = "_blank";
                btn.rel = "sponsored noopener noreferrer";
            }
        }

        // 2. Comparison Tables
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
                           Check Price <span style="font-size: 1.2em;">&rarr;</span>
                        </a>
                    `;
                    updatedCount++;
                }
            }
        });
    }
    console.log(`Links applied. Updated ${updatedCount} table rows.`);
}

// Run immediately if DOM is ready, otherwise wait
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applyAffiliateLinks);
} else {
    applyAffiliateLinks();
}
