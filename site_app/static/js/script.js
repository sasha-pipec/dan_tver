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

burgerWrapper.addEventListener('click', () => {
    burgerWrapper.style.display = 'none';
    body.style.overflow = 'auto';
});

document.addEventListener('DOMContentLoaded', () => {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 'auto',
        spaceBetween: 30,
    });

    var swiper2 = new Swiper('.swiper-container-docs', {
        slidesPerView: 'auto',
        spaceBetween: 16,
    });
});

const header = document.querySelector('.header');
header.classList.add('hidden')
let prevScrollPos = 0;
const handleScroll = () => {

    const currentScrollPos = window.scrollY;

    if(currentScrollPos < 150) {
        header.classList.add('hidden');
    } else {
        if (currentScrollPos > prevScrollPos) {
            header.classList.remove('hidden');
            prevScrollPos = currentScrollPos;
        } else {
            header.classList.add('hidden');
            prevScrollPos = currentScrollPos;
        }
    }
};

window.addEventListener('scroll', handleScroll);