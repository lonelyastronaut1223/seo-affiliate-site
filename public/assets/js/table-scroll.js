// Table Scroll Indicator Handler
// 为移动端表格添加滚动指示器和状态管理

document.addEventListener('DOMContentLoaded', function () {
    const tableWrappers = document.querySelectorAll('.comparison-table-wrapper');

    tableWrappers.forEach(wrapper => {
        // 添加滚动提示属性
        wrapper.setAttribute('data-scroll-hint', 'true');

        // 监听滚动事件
        wrapper.addEventListener('scroll', function () {
            const scrollLeft = this.scrollLeft;
            const scrollWidth = this.scrollWidth;
            const clientWidth = this.clientWidth;

            // 标记已滚动（隐藏提示文字）
            if (scrollLeft > 10) {
                this.classList.add('has-scrolled');
                this.classList.add('scrolled-start');
            } else {
                this.classList.remove('has-scrolled');
                this.classList.remove('scrolled-start');
            }

            // 检查是否滚动到最右边
            if (scrollLeft + clientWidth >= scrollWidth - 10) {
                this.classList.add('scrolled-end');
            } else {
                this.classList.remove('scrolled-end');
            }
        });

        // 初始化状态检查
        const hasOverflow = wrapper.scrollWidth > wrapper.clientWidth;
        if (!hasOverflow) {
            // 如果内容不超出，移除提示
            wrapper.removeAttribute('data-scroll-hint');
        }
    });

    // 响应式检查：窗口resize时重新评估
    let resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
            tableWrappers.forEach(wrapper => {
                const hasOverflow = wrapper.scrollWidth > wrapper.clientWidth;
                if (hasOverflow && window.innerWidth <= 768) {
                    wrapper.setAttribute('data-scroll-hint', 'true');
                    wrapper.classList.remove('has-scrolled');
                } else {
                    wrapper.removeAttribute('data-scroll-hint');
                }
            });
        }, 250);
    });
});
