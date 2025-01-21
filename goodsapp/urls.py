from django.urls import path
from goodsapp import views

urlpatterns = [
    path('', views.IndexView.as_view()),
]