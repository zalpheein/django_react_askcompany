from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get('q', '')

    if q:
        qs = qs.filter(message__icontains=q)

    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q,
    })
 

# 파이썬 3.6부터 지원하는 타입힌트 기능 예시
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        post = Post.objects.get(pk=pk)
    except:
        raise Http404

    return render(request, 'instagram/post_detail.html', {
        'post': post
    })















