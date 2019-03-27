$(function () {
    $('.carousel-indicators li').mouseover(function () {
        // 获取当前索引
        let num = $(this).index();
        console.log(num);
        // $('.carousel-inner .item').eq(num).fadeIn().siblings().fadeOut();
        $('.carousel-indicators li').eq(num).addClass('active').siblings().removeClass('active');
        $('.carousel-inner .item').eq(num).addClass('active').siblings().removeClass('active');
    })
});