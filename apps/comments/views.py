from django.http import JsonResponse, HttpResponse
from django.views.generic import FormView
from django.views.decorators.http import require_POST
from .models import Comment
from blog.models import Article
from comments.email import SendEmail
from .forms import CommentForm
from utils.utils import ip_to_addr, get_user_agent
from celery_tasks.tasks import send_email_by_celery, send_email_by,hello


# Create your views here.
@require_POST
def add_comment(request):
    """评论"""
    if request.is_ajax():
        form = CommentForm(request.POST)
        print(form, 'form')
        if form.is_valid():
            name = form.cleaned_data.get('nickname')
            email = form.cleaned_data.get('email')
            url = form.cleaned_data.get('url')
            content = form.cleaned_data.get('content')
            article_id = form.cleaned_data.get('belong')
            parent_id = form.cleaned_data.get('parent')
            ip, country = ip_to_addr(request)
            browser = get_user_agent(request)
            if parent_id == 0:
                # parent_id为0时表示是父集评论,评论的是文章,不为0时表示是回复
                new_comment = Comment(nickname=name,
                                      email=email,
                                      url=url,
                                      content=content,
                                      belong_id=article_id,
                                      ip_address=country,
                                      browser=browser)
            else:
                new_comment = Comment(nickname=name,
                                      email=email,
                                      url=url,
                                      content=content,
                                      belong_id=article_id,
                                      ip_address=country,
                                      browser=browser,
                                      parent_id=parent_id)
            print(new_comment, 'comment')
            new_comment.save()
            new_point = '#comment-' + str(new_comment.pk)
            send_mail = SendEmail()
            email_data = {
                'comment_name': name,
                'comment_content': content,
                'comment_url': url
            }
            to_list = []
            # 发送给自己（可以写其他邮箱）
            if new_comment.parent:
                # 作者回复
                subject = '来着[Superficial的博客]评论回复'
                template = 'email/reply_email.html'
                to_list.append(email)
                print('回复')
            else:
                print('评论')
                # 如何父集不存在,代表用户评论作者
                subject = '来着[Superficial的博客]博文评论'
                template = 'email/send_email.html'
                to_list.append('347106739@qq.com')
            # send_mail.send_email_by_template(subject, template, email_data, to_list)
            # send_email_by_celery(subject, template, email_data, to_list)
            hello.delay()
            return JsonResponse({'msg': '评论提交成功！', 'new_point': new_point})
        return JsonResponse({'msg': '评论失败！'})
