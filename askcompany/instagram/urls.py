from django.urls import path
from .import views 

# URL Reverse에서 namespace 역할을 하게 됨
app_name = 'instagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail),


]
