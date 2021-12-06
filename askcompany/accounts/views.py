from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render


# FBV 방식 - 프로필
# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')


# CBV 방식 - 프로필
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

profile = ProfileView.as_view()












