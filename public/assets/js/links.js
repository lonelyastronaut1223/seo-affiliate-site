/**
 * AUTO-GENERATED FILE - DO NOT MODIFY DIRECTLY
 * This file is generated from src/config/affiliateLinks.js by scripts/core/sync_links.js
 * Last Updated: 2026-01-26T18:44:48.258Z
 */

const affiliateLinks = {
    "sony-a6700": "https://amzn.to/3NpavhW",
    "sony-a7c-ii": "https://amzn.to/49XHouC",
    "sony-a7-iv": "https://amzn.to/3Zmgs1u",
    "sony-a7iv": "https://amzn.to/3Zmgs1u",
    "sony-zv-e10": "https://amzn.to/3NqCxth",
    "sony-zv-e10-ii": "https://amzn.to/49HqAH3",
    "sony-zv-e1": "https://amzn.to/3Le0oMc",
    "sony-fx3": "https://amzn.to/4b0w6Ha",
    "canon-eos-r8": "https://amzn.to/3Lvm06M",
    "canon-r50": "https://amzn.to/3YBJTwt",
    "canon-r100": "https://amzn.to/45FQ6eA",
    "canon-r6-ii": "https://amzn.to/4sHWE6q",
    "canon-r5-ii": "https://amzn.to/49Qljgl",
    "canon-r6-iii": "https://amzn.to/49XgbqW",
    "nikon-z8": "https://amzn.to/4sMa95c",
    "nikon-z6-iii": "https://amzn.to/4biylFP",
    "fujifilm-x-t5": "https://amzn.to/4qSEPQj",
    "fujifilm-x-s20": "https://amzn.to/3YJrfTj",
    "fujifilm-x100vi": "https://amzn.to/4pGFIdE",
    "fujifilm-x-t50": "https://amzn.to/4pJH5se",
    "panasonic-s5-ii": "https://amzn.to/45FQbyU",
    "panasonic-s5-iix": "https://amzn.to/49nmk0t",
    "panasonic-g100d": "https://amzn.to/4sHwgtm",
    "om-system-om-1-ii": "https://amzn.to/3NFML9c",
    "om-system-om-5": "https://amzn.to/49TF1cd",
    "dji-osmo-pocket-3": "https://amzn.to/3NlCOOg",
    "dji-action-5": "https://amzn.to/4jHiYc3",
    "gopro-13": "https://amzn.to/3Ne6SLE",
    "insta360-x4": "https://amzn.to/4aUs0jM",
    "sigma-56-14": "https://amzn.to/49QDK4N",
    "tamron-17-70": "https://amzn.to/49y4Izb",
    "sony-35-18": "https://amzn.to/4qDP3EE",
    "sony-70-350": "https://amzn.to/45jpD6t",
    "canon-rf-50": "https://amzn.to/3NTbneE",
    "canon-rfs-18-150": "https://amzn.to/49vdOg1",
    "canon-rf-85": "https://amzn.to/4a9hpQ7",
    "canon-rf-24-105": "https://amzn.to/4baLpgA",
    "fuji-xf-16-50": "https://amzn.to/4qC3qJq",
    "fuji-xf56-f12": "https://amzn.to/4pPtlfw",
    "fuji-xf-33": "https://amzn.to/4pSIEE1",
    "sigma-18-50-fuji": "https://amzn.to/4jQ9xHz",
    "peak-travel-tripod": "https://amzn.to/4qw0vBR",
    "manfrotto-befree": "https://amzn.to/4a26V5Y",
    "ulanzi-mt79": "https://amzn.to/3YPknE6",
    "peak-everyday-30": "https://amzn.to/4b5V9IV",
    "lowepro-protactic": "https://amzn.to/3LsLstI",
    "wandrd-prvke": "https://amzn.to/4pZZFfW",
    "sandisk-extreme-pro-256": "https://amzn.to/4sPSPMl",
    "sony-tough-v90": "https://amzn.to/4r2T84M",
    "sandisk-extreme-256": "https://amzn.to/49yP9qQ"
};

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
        document.querySelectorAll(`.btn-buy[data-product="${id}"]`).forEach(btn => updateBtn(btn, link));

        // Strategy C: Comparison tables
        document.querySelectorAll(`a[href="#${id}"]`).forEach(anchor => {
            const row = anchor.closest('tr');
            if (row) {
                const priceCell = row.querySelector('.price-check');
                if (priceCell) {
                    priceCell.innerHTML = `<a href="${link}" target="_blank" rel="sponsored noopener noreferrer" style="color:#10b981;text-decoration:none;font-weight:800;display:inline-flex;align-items:center;gap:4px">${checkPriceText} <span style="font-size:1.2em">&rarr;</span></a>`;
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
