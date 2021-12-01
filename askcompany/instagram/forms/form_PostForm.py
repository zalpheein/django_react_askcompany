from django import forms
# . ⇐ 현재 폴더
# .. ⇐ 현재 폴더의 부모 폴더
# ..models ⇐ 현재 폴더의 부모 폴더 내에 있는 models.py 파일을 의미
# from ..models import Post ⇐ 현재 폴더의 부모 폴더 내에 있는 models.py 에 정의 된 Post 객체
from ..models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        # Post 모델의 전체 필드를 ModelForm 으로 사용
        # fields = '__all__'

        # Post 모델에서 사용자가 선택한 특정 필드를 ModelForm 으로 사용
        # 필수 입력 필드가 문제 될 수 있음.
        fields = ['message', 'photo', 'tag_set', 'is_public']
        # 현재 상태로 저장(veiws.post_new 호출) 시, Post.author 이 필수 입력인데...없으므로
        # post = form.save() 함수 호출시 오류 발생....
        # 이에 form.save() 에 commit=False 인자를 추가하고
        # post.author 정보를 지정하고
        # post.save() 를 호출하여 저장
