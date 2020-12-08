from django.shortcuts import render, redirect
from .models import Cadastro
from .forms import CadastroForm


def list_cadastro(request):
    cadastro = Cadastro.objects.all()
    return render(request, 'cadastro.html', {'cadastro': cadastro})


def create_cadastro(request):
    form = CadastroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_cadastro')

    return render(request, 'cadastro-form.html', {'form': form})


def update_cadastro(request, id):
    cadastro = Cadastro.objects.get(id=id)
    form = CadastroForm(request.POST or None, instance=cadastro)

    if form.is_valid():
        form.save()
        return redirect('list_cadastro')

    return render(request, 'cadastro-form.html', {'form': form, 'cadastro': cadastro})


def delete_cadastro(request, id):
    cadastro = Cadastro.objects.get(id=id)

    if request.method == 'POST':
        cadastro.delete()
        return redirect('list_cadastro')

    return render(request, 'cadastro-delete-confirm.html', {'cadastro': cadastro})
