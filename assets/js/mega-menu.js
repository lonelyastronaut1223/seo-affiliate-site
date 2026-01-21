/**
 * Mega Menu Navigation System
 * Handles dropdown menus, search functionality, and mobile navigation
 */

(function () {
    'use strict';

    // State
    let isScrolled = false;

    // Initialize on DOM load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    function init() {
        initStickyHeader();
        initSearch();
        initMobileMenu();
        initKeyboardNav();
    }

    /**
     * Sticky Header on Scroll
     */
    function initStickyHeader() {
        const header = document.querySelector('header');
        if (!header) return;

        header.classList.add('header-sticky');

        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY > 50;

            if (scrolled !== isScrolled) {
                isScrolled = scrolled;
                header.classList.toggle('header-scrolled', scrolled);
            }
        }, { passive: true });
    }

    /**
     * Search Functionality
     */
    function initSearch() {
        const searchInput = document.querySelector('.header-search input');
        if (!searchInput) return;

        // Search data
        const searchData = [
            // Guides
            { title: 'Best Camera for Beginners', url: 'guides/best-camera-for-beginners-2026.html', category: 'Guides' },
            { title: 'Best Travel Camera', url: 'guides/best-travel-camera.html', category: 'Guides' },
            { title: 'Best Vlog Camera', url: 'guides/best-vlog-camera.html', category: 'Guides' },
            { title: 'Best Budget Camera', url: 'guides/best-budget-camera-under-800.html', category: 'Guides' },
            { title: 'Best Hybrid Camera', url: 'guides/best-hybrid-camera.html', category: 'Guides' },
            { title: 'Best Full-Frame for Video', url: 'guides/best-full-frame-for-video.html', category: 'Guides' },
            { title: 'Best Action & 360 Camera', url: 'guides/best-action-360-camera.html', category: 'Guides' },

            // Reviews
            { title: 'Sony A7C II Review', url: 'reviews/sony-a7c-ii-review.html', category: 'Reviews' },
            { title: 'Sony A7 IV Review', url: 'reviews/sony-a7-iv-review.html', category: 'Reviews' },
            { title: 'Fujifilm X-T5 Review', url: 'reviews/fujifilm-x-t5-review.html', category: 'Reviews' },
            { title: 'Canon EOS R8 Review', url: 'reviews/canon-eos-r8-review.html', category: 'Reviews' },
            { title: 'Sony ZV-E10 Review', url: 'reviews/sony-zv-e10-review.html', category: 'Reviews' },

            // Lenses
            { title: 'Sony E-Mount Lenses', url: 'lenses/best-sony-e-mount-lenses.html', category: 'Lenses' },
            { title: 'Canon RF Lenses', url: 'lenses/best-canon-rf-lenses.html', category: 'Lenses' },
            { title: 'Fujifilm X-Mount Lenses', url: 'lenses/best-fujifilm-x-mount-lenses.html', category: 'Lenses' },

            // Gear
            { title: 'Best Tripods', url: 'gear/best-tripods.html', category: 'Gear' },
            { title: 'Best Camera Bags', url: 'gear/best-camera-bags.html', category: 'Gear' },
            { title: 'Best SD Cards', url: 'gear/best-sd-cards.html', category: 'Gear' }
        ];

        // Create search results container
        const resultsContainer = document.createElement('div');
        resultsContainer.className = 'search-results';
        resultsContainer.style.cssText = `
      position: absolute;
      top: calc(100% + 0.5rem);
      left: 0;
      right: 0;
      background: #0f1a2b;
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 8px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      max-height: 400px;
      overflow-y: auto;
      display: none;
      z-index: 1001;
    `;
        searchInput.parentElement.appendChild(resultsContainer);

        // Search handler
        let searchTimeout;
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            const query = e.target.value.trim().toLowerCase();

            if (query.length < 2) {
                resultsContainer.style.display = 'none';
                return;
            }

            searchTimeout = setTimeout(() => {
                const results = searchData.filter(item =>
                    item.title.toLowerCase().includes(query) ||
                    item.category.toLowerCase().includes(query)
                );

                displaySearchResults(results, resultsContainer, query);
            }, 200);
        });

        // Close on click outside
        document.addEventListener('click', (e) => {
            if (!searchInput.parentElement.contains(e.target)) {
                resultsContainer.style.display = 'none';
            }
        });
    }

    function displaySearchResults(results, container, query) {
        if (results.length === 0) {
            container.innerHTML = `
        <div style="padding: 1.5rem; text-align: center; color: #8b9eb0;">
          No results found for "${query}"
        </div>
      `;
            container.style.display = 'block';
            return;
        }

        const html = results.map(item => `
      <a href="${item.url}" style="
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.875rem 1.25rem;
        color: #f0f4f8;
        text-decoration: none;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        transition: all 200ms ease;
      " onmouseover="this.style.background='rgba(255,255,255,0.05)'" onmouseout="this.style.background='transparent'">
        <span style="font-weight: 500;">${item.title}</span>
        <span style="
          font-size: 0.75rem;
          color: #8b9eb0;
          background: rgba(77, 163, 255, 0.15);
          padding: 0.25rem 0.625rem;
          border-radius: 4px;
        ">${item.category}</span>
      </a>
    `).join('');

        container.innerHTML = html;
        container.style.display = 'block';
    }

    /**
     * Mobile Menu Toggle
     */
    function initMobileMenu() {
        const hamburger = document.querySelector('.hamburger');
        const mobileMenu = document.querySelector('.mobile-menu');
        if (!hamburger || !mobileMenu) return;

        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Mobile submenu toggles
        const headers = mobileMenu.querySelectorAll('.mobile-menu-header');
        headers.forEach(header => {
            header.addEventListener('click', () => {
                const links = header.nextElementSibling;
                const arrow = header.querySelector('.mobile-menu-arrow');

                links.classList.toggle('active');
                if (arrow) {
                    arrow.textContent = links.classList.contains('active') ? '−' : '+';
                }
            });
        });
    }

    /**
     * Keyboard Navigation
     */
    function initKeyboardNav() {
        document.addEventListener('keydown', (e) => {
            // ESC to close mobile menu
            if (e.key === 'Escape') {
                const hamburger = document.querySelector('.hamburger');
                const mobileMenu = document.querySelector('.mobile-menu');

                if (hamburger && hamburger.classList.contains('active')) {
                    hamburger.classList.remove('active');
                    mobileMenu.classList.remove('active');
                    document.body.style.overflow = '';
                }
            }

            // CMD/CTRL + K to focus search
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                const searchInput = document.querySelector('.header-search input');
                if (searchInput) searchInput.focus();
            }
        });
    }
})();
