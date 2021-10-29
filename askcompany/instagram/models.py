from django.db import models

class Post(models.Model):
    message = models.TextField()
    # 실제 저장 폴더
    # root/앱이름/settings.MEDIA_ROOT설정값=media/앱이름/모델명/images/%Y/%m/%d/ 경로에 이미지 파일들 저장
    # 단, 로컬 파일명으로 저장 되므로.. 함수를 사용하여 파일명을 변경 가능함
    photo = models.ImageField(blank=True, upload_to='instagram/post/images/%Y/%m/%d/')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    #__str__ 함수는 객체를 대표하는 문자열 표현을 의미
    def __str__(self):
        #return f"Custom Post object ({self.id})"
        #return f"Custom Post object ({})".format(self.id)
        return self.message
    
    #어드민 리스트에 별도의 컬럼을 추가하는 경우
    def message_length(self):
        return len(self.message)

    #어드민 리스트에 별도의 컬럼명을 영어 --> 한글
    message_length.short_description = "메시지 글자수"
























