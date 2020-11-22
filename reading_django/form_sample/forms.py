from django import forms


class MyForm(forms.Form):
    message = forms.CharField()

    def clean_message(self):
        msg = self.cleaned_data['message']
        if '不正' in msg:
            raise forms.ValidationError('不正な文字列が含まれています')
        return msg
