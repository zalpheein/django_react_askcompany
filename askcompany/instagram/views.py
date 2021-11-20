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


# 상기의 post_detail 은 모든 post를 보여준다.. 
#   로그인 여부와도 상관 없고..
#   공개 여부와도 상관 없이.. 그냥 모두다...
#   그런데.... 만약, 로그인 허용된 사람들에게만 보여 주려고 할 경우엔?
#   또는.... 만약, 공개 허용된 것만 보여 주려고 할 경우엔?
#   이럴때는, 별도로 클래스를 만들고...get_queryset() 함수를 별도로 구현 해야 한다....
# class PostDetailView(DetailView):
#     model = Post

#     # 공개로 지정된 post 만 가져오는 방법
#     # queryset = Post.objects.filter(is_public=True)

#     # 로그인 된 사용자만 post 를 보여주려면?
#     def get_queryset(self):
#         qs = super().get_queryset()
#         if not self.request.user.is_authenticated:
#             qs = qs.filter(is_public=True)
#         return qs











