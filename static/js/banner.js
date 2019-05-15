$(function () {
    var swiper = new Swiper('.carousel', {
        slidesPerView: 1,
        autoplay: {
            delay: 2000,//1秒切换一次
        },
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
});