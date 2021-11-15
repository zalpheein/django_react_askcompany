from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="instagram_post_set")
    message = models.TextField()
    # 실제 저장 폴더
    # root/앱이름/settings.MEDIA_ROOT 설정값=media/앱이름/모델명/images/%Y/%m/%d/ 경로에 이미지 파일들 저장
    # 단, 로컬 파일명으로 저장 되므로.. 함수를 사용하여 파일명을 변경 가능함
    photo = models.ImageField(blank=True, upload_to='instagram/post/images/%Y/%m/%d/')

    # ManyToManyField 지정 방법2 +++++++
    # Python은 스크립트 언어이므로... 순차 실행.. 
    # 현 단계에서 Tag 정보가 정의 되지 않았으므로 Tag 대신 문자열 'Tag'로 정의
    # 만약 그냥 Tag 로 하려고 하면... Post 클래스 정의부 위에 Tag 클래스 정의부가 선언 되어야
    tag_set = models.ManyToManyField('Tag', blank=True)

    is_public = models.BooleanField(default=False, verbose_name='공개여부')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    # __str__ 함수는 객체를 대표하는 문자열 표현을 의미
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        # return f"Custom Post object ({})".format(self.id)
        return self.message
    
    # 어드민 리스트에 별도의 컬럼을 추가하는 경우
    def message_length(self):
        return len(self.message)

    # 어드민 리스트에 별도의 컬럼명을 영어 --> 한글
    message_length.short_description = "메시지 글자수"



class Comment(models.Model):
    #post_id 라는 필드가 실제로 생성됨
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="instagram_comment_set")
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # ManyToManyField 지정 방법1
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

















