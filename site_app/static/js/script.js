const burgerBtnOpen = document.getElementById('open');
const burgerBtnClose = document.getElementById('close');
const burgerWrapper = document.querySelector('.burger-wrapper');
const body = document.body;
burgerBtnOpen.addEventListener('click', () => {
    burgerWrapper.style.display = 'flex';
    body.style.overflow = 'hidden';
});

burgerBtnClose.addEventListener('click', () => {
    burgerWrapper.style.display = 'none';
    body.style.overflow = 'auto';
});

document.addEventListener('DOMContentLoaded', () => {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 'auto',
        spaceBetween: 30,
        loop: true,
    });

    var swiper2 = new Swiper('.swiper-container-docs', {
        slidesPerView: 'auto',
        spaceBetween: 16,
    });
});