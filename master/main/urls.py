from django.urls import path
from . import views

urlpatterns = [
    path('', views.svaz, name='main'),
    path('catalog/', views.cataloge, name='cata'),
    path('<int:pk>', views.Detail.as_view(), name='detail'),
]