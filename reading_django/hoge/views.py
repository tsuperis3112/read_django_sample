from django.http.response import HttpResponse
from django.views import View


def function_based_view(request):
    """関数ベースビュー"""
    return HttpResponse('function_based_view')


class ClassBasedView(View):
    """クラスベースビュー"""
    def get(self, request):
        return HttpResponse('class_based_view GET')

    def post(self, request):
        return HttpResponse('class_based_view POST')
