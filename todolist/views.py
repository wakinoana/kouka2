from django.shortcuts import render
from .forms import InquiryForm

from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    # 表示したいHTMLを指定
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm    
