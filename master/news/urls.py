from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.new, name='news1'),
    path('<int:pk>', views.Detailed.as_view(), name='detail_news'),
]