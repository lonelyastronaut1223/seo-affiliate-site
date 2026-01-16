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

    // Advanced Quiz Logic
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
        // Open
        startQuizBtn.addEventListener('click', () => {
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

        // Simple Decision Tree
        if (userAnswers.type === 'video') {
            if (userAnswers.budget === 'low') {
                recommendation = { name: 'Sony ZV-E10', desc: 'The undisputed king of budget vlogging.', link: 'reviews/sony-zv-e10-review.html' };
            } else if (userAnswers.budget === 'mid') {
                recommendation = { name: 'DJI Osmo Pocket 3', desc: 'The ultimate portable vlog camera.', link: 'reviews/dji-osmo-pocket-3-review.html' };
            } else {
                recommendation = { name: 'Sony ZV-E1', desc: 'Full-frame cinema quality in a tiny body.', link: 'guides/best-vlog-camera.html' };
            }
        } else if (userAnswers.type === 'photo') {
            if (userAnswers.budget === 'low') {
                recommendation = { name: 'Canon R100', desc: 'Super affordable entry into real photography.', link: 'guides/best-camera-for-beginners-2026.html' };
            } else if (userAnswers.budget === 'high') {
                recommendation = { name: 'Sony A7R V', desc: 'The resolution monster for pros.', link: 'guides/best-full-frame-for-video.html' };
            } else {
                recommendation = { name: 'Fujifilm X-T5', desc: 'Pure photography joy with 40MP details.', link: 'reviews/fujifilm-x-t5-review.html' };
            }
        } else { // Hybrid
            if (userAnswers.budget === 'low') {
                recommendation = { name: 'Canon R50', desc: 'Tiny but mighty hybrid for beginners.', link: 'guides/best-camera-for-beginners-2026.html' };
            } else if (userAnswers.exp === 'pro' || userAnswers.budget === 'high') {
                recommendation = { name: 'Sony A7 IV', desc: 'The industry standard for do-it-all work.', link: 'reviews/sony-a7-iv-review.html' };
            } else {
                recommendation = { name: 'Panasonic S5 II', desc: 'Best value full-frame hybrid right now.', link: 'reviews/panasonic-s5-ii-review.html' };
            }
        }

        recContent.innerHTML = `
            <div class="card" style="border:1px solid var(--accent); background:rgba(77,163,255,0.05);">
                <div class="tag" style="background:var(--accent); color:#0a0f1a; font-weight:700; margin-bottom:12px; display:inline-block; padding:4px 8px; border-radius:4px; font-size:11px;">#1 RECOMMENDATION</div>
                <h3 style="margin-top:0; font-size:24px;">${recommendation.name}</h3>
                <p style="font-size:15px; margin-bottom:16px; color:#c6cbe0;">${recommendation.desc}</p>
                <a href="${recommendation.link}" class="buy-btn" style="width:100%; text-align:center; padding:12px;">View Details &rarr;</a>
            </div>`;
    }
});

    // Newsletter Form
    const newsletterForm = document.getElementById('newsletter-form');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = e.target.querySelector('input[type="email"]').value;
            
            // Show success message
            const button = e.target.querySelector('button');
            const originalText = button.textContent;
            button.textContent = '✓ Subscribed!';
            button.style.background = '#4ade80';
            
            // Reset form
            e.target.reset();
            
            // Reset button after 3 seconds
            setTimeout(() => {
                button.textContent = originalText;
                button.style.background = '';
            }, 3000);
            
            // TODO: In production, connect to your email service
            // Examples: Mailchimp, ConvertKit, SendGrid, etc.
            console.log('Newsletter subscription:', email);
        });
    }
});
