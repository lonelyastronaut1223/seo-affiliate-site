/**
 * FAQ Accordion Functionality
 * Provides expand/collapse behavior for FAQ sections on review pages
 */

document.addEventListener('DOMContentLoaded', () => {
    const faqItems = document.querySelectorAll('.faq-item');

    if (faqItems.length === 0) return; // Exit if no FAQ items

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        const toggle = item.querySelector('.faq-toggle');

        if (!question || !answer || !toggle) return;

        // Add click handler to question
        question.addEventListener('click', () => {
            const isOpen = item.classList.contains('active');

            // Close all other FAQ items
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    const otherAnswer = otherItem.querySelector('.faq-answer');
                    const otherToggle = otherItem.querySelector('.faq-toggle');
                    if (otherAnswer) {
                        otherAnswer.style.maxHeight = '0';
                        otherAnswer.classList.remove('open');
                    }
                    if (otherToggle) otherToggle.textContent = '+';
                }
            });

            // Toggle current FAQ item
            if (!isOpen) {
                // Open this item
                item.classList.add('active');
                answer.style.maxHeight = answer.scrollHeight + 'px';
                answer.classList.add('open');
                toggle.textContent = '−';
            } else {
                // Close this item
                item.classList.remove('active');
                answer.style.maxHeight = '0';
                answer.classList.remove('open');
                toggle.textContent = '+';
            }
        });

        // Add keyboard accessibility
        question.setAttribute('role', 'button');
        question.setAttribute('tabindex', '0');
        question.setAttribute('aria-expanded', 'false');

        question.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                question.click();
            }
        });
    });
});
