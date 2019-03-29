$(function () {
    $('.submit').click(function () {
        let btn_target = $(this),
            comment = $("#comment-form textarea[name=comment]").val(),
            author = $("#comment-form input[name=author]"),
            email = $("#comment-form input[name=email]").val(),
            url = $("#comment-form input[name=url]").val();
        if (comment.length === 0) {
            alert('评论内容不能为空!');
            return;
        }
        $.ajax({
            url: "/comment/add_comment/",
            type: 'POST',
            data: {
                'author': author.val(),
                'email': email,
                'url': url,
                'comment': comment,
                'article': author.attr('data-id'),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: 'json',
            success: function (res) {
                btn_target.removeClass("disabled");
                console.log(res);
                sessionStorage.setItem('new_point', res.new_point);
                window.location.reload();
            }
        });
    });

    $('.reply').click(function () {
        let name = $(this).parent().children(':first').text();
        $('.rep-to').text("回复 @" + name).removeClass('hidden');
        // 根据锚点跳转到评论区时增加动画
        $('html,body').animate({
            scrollTop: ($($(this).attr('href')).offset().top - 50)
        }, 500);
    });

    if (sessionStorage.getItem('new_point')) {
        // 评论提交后定位到新评论的位置
        let top = $(sessionStorage.getItem('new_point')).offset().top - 10;
        $('body,html').animate({scrollTop: top}, 200);
        window.location.hash = sessionStorage.getItem('new_point');
        sessionStorage.removeItem('new_point');
    }
    sessionStorage.removeItem('rep_id');
});