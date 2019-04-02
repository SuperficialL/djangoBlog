$(function () {
        let $width = $('.carousel-inner .item').width(),
            curIndex = 0,
            timer = null,
            len = $('.carousel-inner li').length + 1,
            item = $('.carousel-inner li').first().clone();
        $('.carousel-inner').append(item);
        $('.carousel-inner').width(len * $width);
        // 复制第一张图片到最后,实现无缝轮播

        //鼠标划入圆点
        $(".carousel-indicators li").hover(function () {
            let index = $(this).index();
            $(".carousel-inner").stop().animate({
                left: -index * 1000
            }, 500);
            $(this).addClass('active').siblings().removeClass('active');
        });

        /* 右切按钮 */
        $('.next').click(function () {
            curIndex++;
            move()
        });
        /* 左切按钮 */
        $('.prev').click(function () {
            curIndex--;
            move()
        });

        /* 封装 */
        function move() {
            if (curIndex === len) {
                $('.carousel-inner').css({left: 0});
                curIndex = 1
            }
            if (curIndex < 0) {
                $('.carousel-inner').css({
                    left: -(len - 1) * $width + 'px'
                    //判断是第一个li时，无缝连接到最后一个
                });
                curIndex = len - 2;
            }
            $('.carousel-inner').stop().animate({
                left: -curIndex * $width + 'px'
            }, 500);
            if ((curIndex === len - 1)) {
                $('.carousel-indicators li').eq(0).addClass('active').siblings().removeClass('active');
            } else {
                $('.carousel-indicators li').eq(curIndex).addClass('active').siblings().removeClass('active');
            }

        };

        /* 移入banner时取消定时器 */
        $('.carousel').hover(function () {
            clearInterval(timer)
        }, function () {
            timer = setInterval(move, 2000)
        });

        /* 自动轮播 */
        timer = setInterval(function () {
            curIndex++;
            move()
        }, 2000)
    }
);