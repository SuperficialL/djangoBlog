$(function () {
    $('.carousel-indicators li').mouseover(function () {
        // 获取当前索引
        let num = $(this).index(),
            width = $('.carousel').width(),
            moveValue = num * width;
        $('.carousel-inner ul').animate({'right': moveValue}, 500);
        $('.carousel-indicators li').eq(num).addClass('active').siblings().removeClass('active');
        $('.carousel-inner .item').eq(num).addClass('active').siblings().removeClass('active');
    })
});