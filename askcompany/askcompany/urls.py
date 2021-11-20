from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

# 사용자 정의 urlpatterns
api_v1_urlpatterns = [
    # path(...)
]

urlpatterns = [
    # 기본뷰.TemplateView 예시
    # root.settings.TEMPLATES 에 정의 되어야 함.....
    # path('', TemplateView.as_view(template_name='root.html'), name='root'),

    # 기본뷰.RedirectView 예시
    # path('', RedirectView.as_view(url='instagram'), name='root'),
    # 또는
    path('', RedirectView.as_view(
        #url='instagram',
        pattern_name='instagram:post_list',
        ), name='root'),




    path('admin/', admin.site.urls),

    # 사용자 정의 urlpatterns 추가 예시
    # path(‘api/v1 /’, include(api_v1_urlpatterns)),

    path('accounts/', include('accounts.urls')),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    # 장고툴바 설치 후...
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
