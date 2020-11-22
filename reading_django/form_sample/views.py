from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from form_sample.forms import MyForm


class MyFormView(FormView):
    """FormViewサンプル"""
    form_class = MyForm
    success_url = reverse_lazy('form_sample:index')
    template_name = 'form_sample/form_sample.html'

    def form_valid(self, form):
        # バリデーション成功時にメッセージを表示
        msg = form.cleaned_data['message']
        messages.success(self.request, f'フォーム送信を受け付けました: {msg}')
        return super().form_valid(form)
