from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# 사용자 정의 urlpatterns
api_v1_urlpatterns = [
    # path(...)
]

urlpatterns = [
    path('admin/', admin.site.urls),

    # 사용자 정의 urlpatterns 추가 예시
    # path(‘api/v1 /’, include(api_v1_urlpatterns)),

    path('accounts/', include('accounts.urls')),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # 장고툴바 설치 후...
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
