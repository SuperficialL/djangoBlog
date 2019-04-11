$(function () {
    $('.nav-collapse').click(function () {
        $(this).toggleClass('close');
        $('.header .nav').toggleClass('show');
    })
    $(window).scroll(function () {
        let $scroll = $(this).scrollTop();
        if ($scroll > 100) {
            $('#footer .back-top').addClass('back')
        } else {
            $('#footer .back-top').removeClass('back')
        }
    });
    // 回到顶部
    $('#footer .back-top').click(function () {
        $('html,body').animate({
            scrollTop: 0
        }, 800);
    })
});