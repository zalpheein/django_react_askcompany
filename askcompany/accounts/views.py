from django.conf import settings
from django.contrib.auth import get_user_model
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


signup = CreateView.as_view(
    model=User,
    form_class=UserCreationForm,
    success_url=settings.LOGIN_URL,
    template_name='accounts/signup_form.html',
)


# def signup(request):
#     pass


def logout(request):
    pass







