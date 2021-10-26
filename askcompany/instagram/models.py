from django.db import models

class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #__str__ 함수는 객체를 대표하는 문자열 표현을 의미
    def __str__(self):
        #return f"Custom Post object ({self.id})"
        #return f"Custom Post object ({})".format(self.id)
        return self.message
    
    def message_length(self):
        return len(self.message)

    message_length.short_description = "메시지 글자수"
























