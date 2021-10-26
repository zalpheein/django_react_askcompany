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
    pass

