from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
# .forms 는 현재 경로를 의미
# form_PostForm 는 form_PostForm.py 를 의미
# import PostForm 의 PostForm 는 form_PostForm.py 파일의
# class PostForm(forms.ModelForm) 객체인  PostForm 을 의미
from .forms.form_PostForm import PostForm


# FBV 코딩 - 게시글 등록
# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # 검증에 성공한 값들을 사전(dict) 타입으로 반환
#             # post = Post(**form.cleaned_data)
#
#             # 넘겨 받은 값을 수정 도는 변경 하려고 할 경우, form.cleaned_data 을 사용 할것.
#             # message = request.POST['필드명'] <== BAD
#             # message = form.cleaned_data['필드명'] <== GOOD
#
#             post = form.save(commit=False)
#             # request.user = 로그인 사용자를 의미... 그러므로 post_new() 함수는 로그인이 선행되어야 함
#             # 즉, @login_required 라는 장식자를 선언 해두어야 함
#             # 사용자 정의 모델폼 PostForm 이 다채우지 못한 필수 입력값을 채워(여기서는 author 값) 저장 수행
#             post.author = request.user
#             # 만약 IP 주소를 저장 해야할 경우, 모델에 해당 필드를 만들고... request.META['REMOTE_ADDR'] 값을 지정
#             # REMOTE_ADDR 관련 문서
#             #   https://docs.djangoproject.com/en/3.2/ref/request-response/
#
#             # 실제 디비에 저장 되는 시점
#             post.save()
#
#             # 신규 message 생성
#             messages.success(request, '포스팅을 저장했습니다.')
#
#             # models.py 에 정의된 Post 객체 내에 get_absolute_url() 함수가 이미 정의 되어
#             # 있으므로 다음과 같이 호출 가능
#             # 즉, 등록 성공 시 상세뷰 페이지로 이동 노출 됨....
#             return redirect(post)
#             # 하지만, 등록 성공 시, 특정 url 로 가게 하려면??? success_url 을 따로 정의 하여 사용
#             # return redirect('/success_url/')
#     else:
#         form = PostForm()
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': None,
#     })


# CBV 코딩 - 게시글 등록
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    # PostForm 클래스의 fields 에 author 필드가 없으므로..사용자 입력이 없다...
    # 하지만 디비에선 필수 입력인....그래서 form_valid() 함수를 선언
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다.')

        return super().form_valid(form)


post_new = PostCreateView.as_view()


# FBV 코딩 - 게시글 수정
# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     # 여기는 게시글 수정이므로 해당 게시글 작성자와... 현 로그인 사용자가 동일한지 점검 로직 필요
#     if request.user != post.author:
#         messages.error(request, '작성자만 수정할 수 있습니다.')
#         return redirect(post)
#
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             # 검증에 성공한 값들을 dict 타입으로 반환
#             # post = Post(**form.cleaned_data)
#             post = form.save()
#
#             # 신규 message 생성
#             messages.success(request, '포스팅을 수정했습니다.')
#
#             # models.py 에 정의된 Post 객체 내에 get_absolute_url() 함수가 이미 정의 되어
#             # 있으므로 다음과 같이 호출 가능
#             # 즉, 등록 성공 시 상세뷰 페이지로 이동 노출 됨....
#             return redirect(post)
#             # 하지만, 등록 성공 시, 특정 url 로 가게 하려면??? success_url 을 따로 정의 하여 사용
#             # return redirect('/success_url/')
#     else:
#         form = PostForm(instance=post)
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post,
#     })

# CBV 코딩 - 게시글 수정
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    # 본인이 작성한 게시글만 수정 가능 해야 함으로.. 이를 form_valid() 에서 처리
    # 하지만.... 이러한 처리는 기본적으로 데코레이트(@~~)에서 보통 처리 하는 것이 적절함
    # 그래서 본 form_valid() 에서는 제외
    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정 했습니다')
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


# FBV 코딩 - 게시글 삭제
# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     # 삭제 확인 하는 폼을 하나 보여주고....확인 후 삭제
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, '포스팅을 삭제하였습니다.')
#         return redirect('instagram:post_list')
#
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post,
#     })


# CBV 코딩 - 게시글 사제
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram:post_list')


post_delete = PostDeleteView.as_view()


# FBV 코딩
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     # 리스트 노출 시마다, message 신규 생성...큐에 쌓임.... 큐에 쌓인 메시지를 소비하는 루틴도 필요함.
#     # 아래 코드는 message 테스트 목적으로...
#     # messages.success(request, 'message 테스트')
#
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q,
#     })


# CBV 코딩
post_list = ListView.as_view(model=Post, paginate_by=5)

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

# CBV 코딩
post_detail = DetailView.as_view(model=Post)

# 상기의 post_detail 은 모든 게시글을 보여준다..
# 로그인 여부와도 상관 없고..
# 공개 여부와도 상관 없이.. 그냥 모두다...
# 그런데.... 만약, 로그인 허용된 사람들에게만 보여 주려고 할 경우엔?
# 또는.... 만약, 공개 허용된 것만 보여 주려고 할 경우엔?
# 이럴때는, 별도로 클래스를 만들고...get_queryset() 함수를 별도로 구현 해야 한다....

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

#    만약, 템플릿(즉, html 파일)에 추가 내용을 전달 하려고 하면….
#    get_context_data() 함수를 사용...
#    템플릿(즉, html 파일)에서 사용할 내용들을 사전(dictionary) 형태로 미리 준비 하는 함수…. 
#    이 함수에 사전 형태도 정의 해두면…템플릿 즉 html 파일에서 사용 가능
#       def get_context_data(self):
#           pass
