$(function () {
    $('.carousel-indicators li').mouseover(function () {
        // 获取当前索引
        let num = $(this).index();
        $('.carousel-indicators li').eq(num).addClass('active').siblings().removeClass('active');
        $('.carousel-inner .item').eq(num).addClass('active').siblings().removeClass('active');
    })
});