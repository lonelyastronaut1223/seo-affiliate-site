
/**
 * Internationalization Utilities
 * Uses explicit path mappings for accurate hreflang generation
 */

// Full path mappings (EN -> DE)
const pageMapping: Record<string, string> = {
    // Home
    "/": "/de/",

    // Guides
    "/guides/best-camera-for-beginners-2026": "/de/ratgeber/beste-kamera-fuer-anfaenger-2026",
    "/guides/best-travel-camera": "/de/ratgeber/beste-reisekamera",
    "/guides/best-vlog-camera": "/de/ratgeber/beste-vlog-kamera",
    "/guides/best-budget-camera-under-800": "/de/ratgeber/beste-budget-kamera-unter-800",
    "/guides/best-hybrid-camera": "/de/ratgeber/beste-hybrid-kamera",
    "/guides/best-full-frame-for-video": "/de/ratgeber/beste-vollformat-fuer-video",
    "/guides/best-action-360-camera": "/de/ratgeber/beste-action-360-kamera",

    // Reviews (use same slug)
    "/reviews/sony-a7c-ii-review": "/de/reviews/sony-a7c-ii-review",
    "/reviews/sony-a7-iv-review": "/de/reviews/sony-a7-iv-review",
    "/reviews/fujifilm-x-t5-review": "/de/reviews/fujifilm-x-t5-review",
    "/reviews/canon-eos-r8-review": "/de/reviews/canon-eos-r8-review",
    "/reviews/sony-zv-e10-review": "/de/reviews/sony-zv-e10-review",
    "/reviews/nikon-z8-review": "/de/reviews/nikon-z8-review",
    "/reviews/panasonic-s5-ii-review": "/de/reviews/panasonic-s5-ii-review",
    "/reviews/dji-osmo-pocket-3-review": "/de/reviews/dji-osmo-pocket-3-review",
    "/reviews/nikon-z6-iii-review": "/de/reviews/nikon-z6-iii-review",
    "/reviews/canon-r5-ii-review": "/de/reviews/canon-r5-ii-review",
    "/reviews/fujifilm-x-s20-review": "/de/reviews/fujifilm-x-s20-review",
    "/reviews/om-system-om-1-ii-review": "/de/reviews/om-system-om-1-ii-review",
    "/reviews/sony-a7-v-review": "/de/reviews/sony-a7-v-review",

    // Lenses
    "/lenses/best-sony-e-mount-lenses": "/de/objektive/beste-sony-e-mount-objektive",
    "/lenses/best-canon-rf-lenses": "/de/objektive/beste-canon-rf-objektive",
    "/lenses/best-fujifilm-x-mount-lenses": "/de/objektive/beste-fujifilm-x-mount-objektive",

    // Gear
    "/gear/best-tripods": "/de/zubehoer/beste-stative",
    "/gear/best-camera-bags": "/de/zubehoer/beste-kamerataschen",
    "/gear/best-sd-cards": "/de/zubehoer/beste-sd-karten",

    // Comparisons
    "/compare/sony-a7-iv-vs-canon-r6-ii": "/de/vergleiche/sony-a7-iv-vs-canon-r6-ii",
    "/compare/sony-a7-v-vs-canon-r6-iii": "/de/vergleiche/sony-a7-v-vs-canon-r6-iii",
    "/compare/sony-zv-e10-vs-sony-a6700": "/de/vergleiche/sony-zv-e10-vs-sony-a6700",
    "/compare/fujifilm-x-s20-vs-fujifilm-x-t5": "/de/vergleiche/fujifilm-x-s20-vs-fujifilm-x-t5",

    // Static pages
    "/about": "/de/ueber-uns",
    "/contact": "/de/kontakt",
    "/privacy": "/de/datenschutz",
    "/deals": "/de/angebote",
    "/terms": "/de/agb",
};

// Build reverse mapping (DE -> EN)
const reverseMapping: Record<string, string> = {};
for (const [en, de] of Object.entries(pageMapping)) {
    reverseMapping[de] = en;
}

/**
 * Normalize path for consistent lookup (remove trailing slash except for root)
 */
function normalizePath(path: string): string {
    if (path === "/" || path === "/de/") return path;
    return path.replace(/\/$/, "");
}

/**
 * Gets the alternate language URL for a given path
 */
export function getAlternatePath(pathname: string): string {
    const normalized = normalizePath(pathname);
    const isGerman = pathname.startsWith('/de/');

    if (isGerman) {
        // DE -> EN
        return reverseMapping[normalized] || "/";
    } else {
        // EN -> DE
        return pageMapping[normalized] || "/de/";
    }
}

/**
 * Normalizes a URL for canonical tags (handling trailing slashes consistently)
 */
export function normalizeUrl(url: string | URL, base: string = 'https://cameraupick.com'): string {
    const urlObj = typeof url === 'string' ? new URL(url, base) : url;
    let path = urlObj.pathname.replace(/\/$/, '');
    if (path === '') path = ''; // Root
    return `${base}${path}`;
}
