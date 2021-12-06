from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    # 심플 예
    # answer = forms.IntegerField()
    answer = forms.IntegerField(help_text='3 + 3 = ?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer')
        if answer != 6:
            raise forms.ValidationError('땡~~~')

        return answer
