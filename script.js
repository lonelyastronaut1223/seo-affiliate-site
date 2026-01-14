// Year display
document.getElementById("year").textContent = new Date().getFullYear();

// Scroll-to-top button
const toTopBtn = document.getElementById("toTop");
const prefersReducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Debounced scroll handler for better performance
let scrollTimeout;
window.addEventListener("scroll", () => {
    if (scrollTimeout) clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(() => {
        toTopBtn.classList.toggle("show", window.scrollY > 400);
    }, 100);
});

toTopBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: prefersReducedMotion ? "auto" : "smooth"
    });
});

// Image loading optimization
document.addEventListener("DOMContentLoaded", () => {
    const images = document.querySelectorAll("img[loading='lazy']");

    images.forEach(img => {
        const thumb = img.closest('.card-thumb');
        if (thumb) {
            thumb.classList.add('loading');

            img.addEventListener('load', () => {
                thumb.classList.remove('loading');
            });

            // Remove loading class if image fails to load
            img.addEventListener('error', () => {
                thumb.classList.remove('loading');
            });
        }
    });

    // Highlight Language
    const currentPath = window.location.pathname;
    const langNav = document.querySelector("nav[aria-label='Language']");
    if (langNav) {
        const isGerman = currentPath.includes("/de/");
        const langLinks = langNav.querySelectorAll("a");

        langLinks.forEach(link => {
            const linkText = link.textContent.trim();
            if (isGerman && linkText === "DE") {
                link.classList.add("active");
            } else if (!isGerman && linkText === "EN") {
                link.classList.add("active");
            }
        });
    }
});
