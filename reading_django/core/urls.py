"""reading_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from hoge import views as hoge_views

urlpatterns = [
    path('func/', hoge_views.function_based_view, name='hoge_func'),
    path('cls/', hoge_views.ClassBasedView.as_view(), name='hoge_cls'),
    path('form_sample/', include('form_sample.urls')),
]
