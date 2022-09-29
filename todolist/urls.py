from django.urls import path

from .import views

# アプリケーション名
app_name = 'ToDo'
urlpatterns = [
    # ''にアクセスされたらviews.pyのIndexViewを実行
    # ページ名はindex
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),

]
