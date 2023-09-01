from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import *

def svaz(request):
    if request.method == 'POST':
        form = Forma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = Forma()
    return render(request, 'main/html/index.html', {'form': form})

def cataloge(request):
    return render(request, 'main/html/catalogue.html', {'cata': Catalog_models.objects.all()})


class Detail(DetailView):
    model = Catalog_models
    template_name = 'main/html/full_catalog.html'
    context_object_name = 'catalog'