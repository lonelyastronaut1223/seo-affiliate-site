/**
 * Anime.js Animations for cameraupick.com
 * Tasteful micro-interactions that enhance user experience
 */

// Wait for DOM and anime.js to load
document.addEventListener('DOMContentLoaded', () => {

    // Skip animations if user prefers reduced motion
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        return;
    }

    // ============================================
    // Hero Section Entrance Animation
    // ============================================
    if (typeof anime !== 'undefined') {

        // Hero title and subtitle stagger animation
        anime({
            targets: '.hero h1, .hero .hero-sub',
            translateY: [30, 0],
            opacity: [0, 1],
            duration: 800,
            delay: anime.stagger(150),
            easing: 'easeOutCubic'
        });

        // Hero image fade and scale
        anime({
            targets: '.hero-media img, .hero-media picture',
            scale: [0.95, 1],
            opacity: [0, 1],
            duration: 1000,
            delay: 300,
            easing: 'easeOutCubic'
        });

        // ============================================
        // Scroll-triggered Card Animations
        // ============================================
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const animateOnScroll = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                    entry.target.classList.add('animated');

                    // Animate cards in the grid
                    const cards = entry.target.querySelectorAll('.card, .card-plain');
                    if (cards.length > 0) {
                        anime({
                            targets: cards,
                            translateY: [40, 0],
                            opacity: [0, 1],
                            duration: 600,
                            delay: anime.stagger(100, { start: 100 }),
                            easing: 'easeOutQuad'
                        });
                    }

                    // Animate score cards
                    const scores = entry.target.querySelectorAll('.score-card');
                    if (scores.length > 0) {
                        anime({
                            targets: scores,
                            scale: [0.8, 1],
                            opacity: [0, 1],
                            duration: 500,
                            delay: anime.stagger(80),
                            easing: 'easeOutBack'
                        });
                    }

                    // Animate comparison tables
                    const tables = entry.target.querySelectorAll('.comparison, .compare-table');
                    if (tables.length > 0) {
                        anime({
                            targets: tables,
                            translateY: [20, 0],
                            opacity: [0, 1],
                            duration: 600,
                            easing: 'easeOutQuad'
                        });
                    }
                }
            });
        }, observerOptions);

        // Observe all sections
        document.querySelectorAll('.section').forEach(section => {
            // Set initial state
            section.querySelectorAll('.card, .card-plain, .score-card').forEach(el => {
                el.style.opacity = '0';
            });
            animateOnScroll.observe(section);
        });

        // ============================================
        // Button Hover Micro-interactions
        // ============================================
        document.querySelectorAll('.btn, .btn-buy, .buy-btn').forEach(btn => {
            btn.addEventListener('mouseenter', () => {
                anime({
                    targets: btn,
                    scale: 1.02,
                    duration: 200,
                    easing: 'easeOutQuad'
                });
            });

            btn.addEventListener('mouseleave', () => {
                anime({
                    targets: btn,
                    scale: 1,
                    duration: 200,
                    easing: 'easeOutQuad'
                });
            });
        });

        // ============================================
        // Score Counter Animation
        // ============================================
        const scoreObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                    entry.target.classList.add('counted');
                    const targetValue = parseFloat(entry.target.textContent);

                    if (!isNaN(targetValue)) {
                        const obj = { value: 0 };
                        anime({
                            targets: obj,
                            value: targetValue,
                            round: 10,
                            duration: 1500,
                            easing: 'easeOutExpo',
                            update: () => {
                                entry.target.textContent = obj.value.toFixed(1);
                            }
                        });
                    }
                }
            });
        }, { threshold: 0.5 });

        document.querySelectorAll('.score').forEach(score => {
            scoreObserver.observe(score);
        });

        // ============================================
        // Spec Value Number Animation
        // Animates numbers in spec-value elements (e.g., 33MP, 4K60, 5.5 stops)
        // ============================================
        const specValueObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
                    entry.target.classList.add('counted');
                    const originalText = entry.target.textContent.trim();

                    // Extract leading number (supports decimals)
                    const numMatch = originalText.match(/^([\d.]+)/);
                    if (numMatch) {
                        const targetValue = parseFloat(numMatch[1]);
                        const suffix = originalText.slice(numMatch[1].length); // e.g., "MP FF", "fps", " stops"
                        const isDecimal = numMatch[1].includes('.');

                        if (!isNaN(targetValue) && targetValue > 0) {
                            const obj = { value: 0 };
                            anime({
                                targets: obj,
                                value: targetValue,
                                round: isDecimal ? 10 : 1,
                                duration: 1200,
                                easing: 'easeOutExpo',
                                update: () => {
                                    if (isDecimal) {
                                        entry.target.textContent = obj.value.toFixed(1) + suffix;
                                    } else {
                                        entry.target.textContent = Math.round(obj.value) + suffix;
                                    }
                                }
                            });
                        }
                    }
                }
            });
        }, { threshold: 0.3 });

        document.querySelectorAll('.spec-value').forEach(specValue => {
            specValueObserver.observe(specValue);
        });

        // ============================================
        // Navigation Link Hover Effect
        // ============================================
        document.querySelectorAll('.topbar nav a').forEach(link => {
            link.addEventListener('mouseenter', () => {
                anime({
                    targets: link,
                    translateY: -2,
                    duration: 150,
                    easing: 'easeOutQuad'
                });
            });

            link.addEventListener('mouseleave', () => {
                anime({
                    targets: link,
                    translateY: 0,
                    duration: 150,
                    easing: 'easeOutQuad'
                });
            });
        });

        // ============================================
        // Pros/Cons List Stagger Animation
        // ============================================
        const prosConsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                    entry.target.classList.add('animated');
                    const items = entry.target.querySelectorAll('li');

                    anime({
                        targets: items,
                        translateX: [20, 0],
                        opacity: [0, 1],
                        duration: 400,
                        delay: anime.stagger(50),
                        easing: 'easeOutQuad'
                    });
                }
            });
        }, { threshold: 0.3 });

        document.querySelectorAll('.pros ul, .cons ul').forEach(list => {
            list.querySelectorAll('li').forEach(li => li.style.opacity = '0');
            prosConsObserver.observe(list);
        });

        // ============================================
        // Back to Top Button Animation
        // ============================================
        const toTopBtn = document.getElementById('toTop');
        if (toTopBtn) {
            toTopBtn.addEventListener('click', () => {
                anime({
                    targets: toTopBtn,
                    scale: [1, 0.9, 1.1, 1],
                    duration: 400,
                    easing: 'easeInOutQuad'
                });
            });
        }

        console.log('✨ Anime.js animations loaded');
    }
});
