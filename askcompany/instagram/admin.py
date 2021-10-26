from django.contrib import admin
from .models import Post

#등록방법1 - 기본 ModelAdmin 으로 동작
#admin.site.register(Post)


#등록방법2 - 지정 ModelAdmin 으로 동작
#class PostAdmin(admin.ModelAdmin):
#    pass
#
#admin.site.register(Post, PostAdmin)


# 등록방법3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['id', 'message']
    list_filter = ['created_at', 'is_public']    #리스트 우측에 필터영역 생김(영역내 AND 조건..)
    search_fields = ['message']     #검색어 입력 영역 생김 


























