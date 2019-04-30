$(function () {
    let curIndex = 0,
        slider = $(".carousel-inner"),
        totalSlides = $(".carousel-inner .item").length,
        sliderWidth = $(".carousel-inner .item").width(),
        dots = $(".carousel-indicators li"),
        btn_prev = $('.prev'),
        btn_next = $('.next'),
        timer = null;

    // 设置总宽度
    slider.width(sliderWidth * totalSlides);

    // 下一张图片
    btn_next.click(function () {
        slideRight();
    });

    // 上一张图片
    btn_prev.click(function () {
        slideLeft();
    });


    dots.mouseenter(function () {
        curIndex = $(this).index();
        $(this).addClass('active').siblings().removeClass("active");
        slider.animate({'left': -(curIndex * sliderWidth)});
    });

    // 自动轮播
    timer = setInterval(slideRight, 3000);
    slider.hover(
        function () {
            clearInterval(timer);
        }, function () {
            timer = setInterval(slideRight, 3000);
        }
    );

    function slideLeft() {
        curIndex--;
        if (curIndex === -1) {
            curIndex = totalSlides - 1;
        }
        slider.animate({'left': -(sliderWidth * curIndex)});
        dots.removeClass('active').eq(curIndex).addClass('active');
    }

    function slideRight() {
        curIndex++;
        if (curIndex === totalSlides) {
            curIndex = 0;
        }
        slider.animate({'left': -(sliderWidth * curIndex)});
        dots.removeClass('active').eq(curIndex).addClass('active');
    }
});
