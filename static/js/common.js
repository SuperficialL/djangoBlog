$(function () {
        $('.show').click(function () {
            // 显示
            $('#nav-list').toggle();
            $(this).toggleClass('open');
        });
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
    }
);