from django.shortcuts import render

from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    # 表示したいHTMLを指定
    template_name = "index.html"
