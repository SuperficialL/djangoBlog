from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Comment
from .forms import CommentForm
from utils.utils import ip_to_addr, get_user_agent


# Create your views here.

@require_POST
def add_comment(request):
    """评论"""
    if request.is_ajax():
        form = CommentForm(request.POST)
        print(form, 'form')
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            url = form.cleaned_data.get('url')
            content = form.cleaned_data.get('content')
            article_id = form.cleaned_data.get('article')
            ip, country = ip_to_addr(request)
            browser = get_user_agent(request)
            new_comment = Comment(name=name,
                                  email=email,
                                  url=url,
                                  content=content,
                                  article_id=article_id,
                                  ip_addr=country,
                                  browser=browser)
            new_comment.save()
            new_point = '#comment-' + str(new_comment.pk)
            return JsonResponse({'msg': '评论提交成功！', 'new_point': new_point})
        return JsonResponse({'msg': '评论失败！'})
