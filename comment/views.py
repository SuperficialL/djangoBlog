from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Comment


# Create your views here.

@require_POST
def add_comment(request):
    """评论"""
    if request.is_ajax():
        name = request.POST['author']
        email = request.POST['email']
        url = request.POST['url']
        comment = request.POST['comment']
        article_id = request.POST['article']
        new_comment = Comment(
            name=name, email=email, url=url, content=comment, article_id=article_id
        )
        new_comment.save()
        new_point = '#comment-' + str(new_comment.pk)
        return JsonResponse({'msg': '评论提交成功！', 'new_point': new_point})
    return JsonResponse({'msg': '评论失败！'})
