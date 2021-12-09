from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .import views
from .forms.LoginForm import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(
        # form_class=AuthenticationForm, # 명시하지 않으면...내부적으로 AuthenticationForm 을 사용하는 form_class 임
        form_class=LoginForm,            # 사용자 정의 LoginForm...
        template_name='accounts/login_form.html'
    ), name='login'),
    # path('logout/', views.logout, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    path('signup/', views.signup, name='signup'),

]
