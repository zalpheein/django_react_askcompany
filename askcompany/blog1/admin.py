from django.contrib import admin
from .models import Post

#등록방법1 - 기본 ModelAdmin 으로 동작
admin.site.register(Post)
