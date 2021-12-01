import re

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

        # 개별 field 에 대한 유효성 검증 로직을 추가 하려면 def clean_필드명() 함수를 추가로 정의
        # 이는 form.is_valid() 할때 자동 호출 됨
        def clean_message(self):
            message = self.cleaned_data.get['message']
            if message:
                # 검증 / 변환 로직 추가
                # message 변수에 사용된 모든 영어 알파벳을 제거 하는 로직
                message = re.sub(r'[a-zA-Z]+', '', message)
            return message

        def clean_photo(self):
            pass

        # 이러한 검증은 개별 필드에 대한 점검인데... n개 필드를 같이 점검 하려고 할 경우엔?
        def clean(self):
            pass
