from django.shortcuts import render

from .models import Panda
from .forms import BasicForm, PandaForm


def index(request):
    if request.method == 'POST':
        # Bound form
        form = BasicForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
    else:
        # Unbound form
        form = BasicForm()

    print(form.is_bound)
    return render(request, 'index.html', locals())


def panda(request):
    if request.method == 'POST':
        form = PandaForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = PandaForm()

    pandas = Panda.objects.all()
    return render(request, 'panda.html', locals())
