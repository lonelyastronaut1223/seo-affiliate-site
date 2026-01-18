document.addEventListener('DOMContentLoaded', () => {
    // Current year updater
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }

    // Scroll to Top Button
    const toTopBtn = document.getElementById('toTop');
    if (toTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                toTopBtn.classList.add('visible');
            } else {
                toTopBtn.classList.remove('visible');
            }
        });

        toTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Advanced Quiz Logic - German Version
    const startQuizBtn = document.getElementById('start-quiz');
    const closeQuizBtn = document.getElementById('close-quiz');
    const quizModal = document.getElementById('quiz-modal');
    const steps = [
        document.getElementById('quiz-step-1'),
        document.getElementById('quiz-step-2'),
        document.getElementById('quiz-step-3'),
        document.getElementById('quiz-result')
    ];
    const recContent = document.getElementById('recommendation-content');
    const restartBtn = document.getElementById('restart-quiz');

    // State
    let userAnswers = {
        type: '', // video, photo, hybrid
        exp: '',  // beginner, enthusiast, pro
        budget: '' // low, mid, high
    };

    if (startQuizBtn && quizModal) {
        console.log('✅ Quiz (DE): Elemente gefunden. Listener werden hinzugefügt.');

        // Open
        startQuizBtn.addEventListener('click', () => {
            console.log('🔘 Quiz gestartet');
            quizModal.style.display = 'block';
            startQuizBtn.parentElement.style.display = 'none'; // Hide CTA
            showStep(0);
        });

        // Close
        closeQuizBtn.addEventListener('click', resetQuiz);

        // Step 1: Type
        document.querySelectorAll('#quiz-step-1 .quiz-option').forEach(btn => {
            btn.addEventListener('click', () => {
                userAnswers.type = btn.getAttribute('data-type');
                showStep(1);
            });
        });

        // Step 2: Experience
        document.querySelectorAll('#quiz-step-2 .quiz-option').forEach(btn => {
            btn.addEventListener('click', () => {
                userAnswers.exp = btn.getAttribute('data-exp');
                showStep(2);
            });
        });

        // Step 3: Budget & Result
        document.querySelectorAll('#quiz-step-3 .quiz-option').forEach(btn => {
            btn.addEventListener('click', () => {
                userAnswers.budget = btn.getAttribute('data-budget');
                calculateResult();
                showStep(3);
            });
        });

        // Restart
        if (restartBtn) {
            restartBtn.addEventListener('click', () => {
                showStep(0);
            });
        }
    } else {
        if (document.getElementById('camera-finder')) {
            console.warn('⚠️ Quiz (DE): Elemente nicht gefunden.');
        }
    }

    function showStep(index) {
        steps.forEach((step, i) => {
            if (step) step.style.display = i === index ? 'block' : 'none';
        });
    }

    function resetQuiz() {
        quizModal.style.display = 'none';
        startQuizBtn.parentElement.style.display = 'flex'; // Show CTA again
        showStep(0);
    }

    function calculateResult() {
        let recommendation = {};

        // Decision Tree - German Links to German Pages
        if (userAnswers.type === 'video') {
            if (userAnswers.budget === 'low') {
                recommendation = {
                    name: 'Sony ZV-E10',
                    desc: 'Der unangefochtene König des Budget-Vloggings.',
                    link: 'bewertungen/sony-zv-e10-testbericht.html'
                };
            } else if (userAnswers.budget === 'mid') {
                recommendation = {
                    name: 'DJI Osmo Pocket 3',
                    desc: 'Die ultimative tragbare Vlog-Kamera.',
                    link: 'bewertungen/dji-osmo-pocket-3-testbericht.html'
                };
            } else {
                recommendation = {
                    name: 'Sony FX3',
                    desc: 'Vollformat-Kinoqualität in einem kompakten Gehäuse.',
                    link: 'ratgeber/beste-vollformat-fuer-video.html'
                };
            }
        } else if (userAnswers.type === 'photo') {
            if (userAnswers.budget === 'low') {
                recommendation = {
                    name: 'Canon EOS R8',
                    desc: 'Günstiger Einstieg in die Vollformat-Fotografie.',
                    link: 'ratgeber/beste-kamera-fuer-anfaenger-2026.html'
                };
            } else if (userAnswers.budget === 'high') {
                recommendation = {
                    name: 'Nikon Z8',
                    desc: 'Das Auflösungs-Monster für Profis.',
                    link: 'bewertungen/nikon-z8-testbericht.html'
                };
            } else {
                recommendation = {
                    name: 'Fujifilm X-T5',
                    desc: 'Reine Fotografiefreude mit 40MP Details.',
                    link: 'bewertungen/fujifilm-x-t5-testbericht.html'
                };
            }
        } else { // Hybrid
            if (userAnswers.budget === 'low') {
                recommendation = {
                    name: 'Sony ZV-E10',
                    desc: 'Kompakter Hybrid für Einsteiger mit tollem AF.',
                    link: 'bewertungen/sony-zv-e10-testbericht.html'
                };
            } else if (userAnswers.exp === 'pro' || userAnswers.budget === 'high') {
                recommendation = {
                    name: 'Sony A7 IV',
                    desc: 'Der Industriestandard für Alles-Könner.',
                    link: 'bewertungen/sony-a7-iv-testbericht.html'
                };
            } else {
                recommendation = {
                    name: 'Panasonic S5 II',
                    desc: 'Bestes Preis-Leistungs-Verhältnis für Vollformat-Hybride.',
                    link: 'bewertungen/panasonic-s5-ii-testbericht.html'
                };
            }
        }

        recContent.innerHTML = `
            <div class="card" style="border:1px solid var(--accent); background:rgba(77,163,255,0.05);">
                <div class="tag" style="background:var(--accent); color:#0a0f1a; font-weight:700; margin-bottom:12px; display:inline-block; padding:4px 8px; border-radius:4px; font-size:11px;">#1 EMPFEHLUNG</div>
                <h3 style="margin-top:0; font-size:24px;">${recommendation.name}</h3>
                <p style="font-size:15px; margin-bottom:16px; color:#c6cbe0;">${recommendation.desc}</p>
                <a href="${recommendation.link}" class="buy-btn" style="width:100%; text-align:center; padding:12px;">Details ansehen &rarr;</a>
            </div>`;
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
