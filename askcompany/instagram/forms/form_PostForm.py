from django import forms
# . ⇐ 현재 폴더
# .. ⇐ 현재 폴더의 부모 폴더
# ..models ⇐ 현재 폴더의 부모 폴더 내에 있는 models.py 파일을 의미
# from ..models import Post ⇐ 현재 폴더의 부모 폴더 내에 있는 models.py 에 정의 된 Post 객체
from ..models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
