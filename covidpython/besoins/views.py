from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormulaireBesoin


def definir_besoin(request):
    if request.method == 'POST':
        form = FormulaireBesoin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')
        else:

            return redirect(form.errors)
    else:
        form = FormulaireBesoin()
        args = {'form': form}
        return render(request, 'formulaire.html', args)
