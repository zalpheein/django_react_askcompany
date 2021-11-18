from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
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
# FBV 예시 --> CBV 예시는 다음 항목에...
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except:
#     #     raise Http404
#     post = Post.get_object_or_404(pk=pk)

#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#     })

post_detail = DetailView.as_view(model=Post)













