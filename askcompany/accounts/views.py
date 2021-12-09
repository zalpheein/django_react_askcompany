from django.conf import settings
from django.contrib.auth import get_user_model, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from .models import Profile
from .forms.ProfileForm import ProfileForm

# FBV 방식 - 프로필
# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')


# CBV 방식 - 프로필
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()


@login_required
def profile_edit(request):
    try:
        # profile = Profile.objects.get(user=request.user)
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_form.html', {
        'form': form,
    })


# # 단순히 회원 가입만 할경우..... 현재 로직으로는 회원가입 후 로그인까지 한번에 되지 않음
# signup = CreateView.as_view(
#     model=User,
#     # 여기 UserCreationForm 에 사용자 입력 받은 정보가 저장 되어 있음.
#     form_class=UserCreationForm,
#     success_url=settings.LOGIN_URL,
#     template_name='accounts/signup_form.html',
# )


# 회원가입과 로그인 처리를 동시에...
class SignupView(CreateView):
    # 회원 가입 영역
    model = User
    # 여기 UserCreationForm 에 사용자 입력 받은 정보가 저장 되어 있음.
    form_class = UserCreationForm
    # success_url = settings.LOGIN_URL
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'accounts/signup_form.html'

    # 로그인 처리 영역
    def form_valid(self, form):
        response = super().form_valid(form) # 부모를 호출해서 응답을 받아 내고
        user = self.object    # self.object() <== 방금 회원가입한 유저
        auth_login(self.request, user)  # user 를 auth_login 에 처리 요청

        return response


signup = SignupView.as_view()




def logout(request):
    pass







