$(function () {
        $('.fa-navicon').click(function () {
            // 显示
            $('#nav-list').show();
            $('body').addClass('show');
            $('.fa fa-remove').show()
        });
        $('.fa-remove').click(function () {
            // 隐藏
            $('#nav-list').hide();
            $('body').removeClass('show')
        });
        $(window).scroll(function () {
            let $scroll = $(this).scrollTop();
            if ($scroll > 100) {
                $('#footer .back-top').addClass('back')
            } else {
                $('#footer .back-top').removeClass('back')
            }
        });
        // 搜索显示隐藏
        $('.fa-search').click(function () {
            $('.search').toggleClass('show').focus();
        });
        // 搜索
        $('.search').keyup(function (event) {
            if (event.keyCode === 13) {
                q = $(this).children('input').val();
                if (q) {
                    $(this).submit()
                } else {
                    return false
                }
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