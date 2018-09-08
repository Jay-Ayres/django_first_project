from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pessoa
from .forms import PersonForm


# Create your views here.

@login_required
def persons_list(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'pessoa_form.html', {'form': form})

@login_required
def person_update(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PersonForm(request.POST or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'pessoa_form.html', {'form': form})

@login_required
def person_delete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    form = PersonForm(request.POST or None, instance=pessoa)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('persons_list')
    return render(request, 'person_delete_confirm.html', {'form': form})