from django.contrib import admin
from django.utils.safestring import mark_safe
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
    #노출을 원하는 필드명 리스트
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']

    #상세 페이지로 들어갈 링크 대상 필드 지정
    list_display_links = ['id', 'message']

    #리스트 우측에 필터영역 생김(영역내 AND 조건..)
    list_filter = ['created_at', 'is_public']

    #검색어 입력 영역 생김 
    search_fields = ['message']


    def photo_tag(self, post):
        if post.photo:
            #return f'<img src="{post.photo.url}" />'    #html 태그를 그대로 노출
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px" />')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글짜"


























