from django.shortcuts import render, redirect
from inscription.forms import FormulaireInscription


def inscription(request):
    if request.method == 'POST':
        form = FormulaireInscription(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')
        else:

            return redirect(form.errors)
    else:
        form = FormulaireInscription()
        args = {'form': form}
        return render(request, 'index.html', args)
