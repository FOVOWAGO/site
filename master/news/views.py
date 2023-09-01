from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

def new(request):
    return render(request, 'news/html/novosti.html', {'news123': Novosti_models.objects.all()})



class Detailed(DetailView):
    model = Novosti_models
    template_name = 'news/html/full_news.html'
    context_object_name = 'novost'