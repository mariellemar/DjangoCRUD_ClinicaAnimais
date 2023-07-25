from django.shortcuts import render, redirect
from .models import Animal

def home(request):
    animais = Animal.objects.all()

    return render(request, "index.html", {"animais": animais})

def salvar(request):
    nome = request.POST.get("nome")
    especie = request.POST.get("especie")
    nome_dono = request.POST.get("nome_dono")
    telefone = request.POST.get("telefone")

    Animal.objects.create(nome=nome,
                          especie=especie,
                          nome_dono=nome_dono,
                          telefone=telefone)
    animais = Animal.objects.all()

    return render(request, "index.html", {"animais": animais})

def editar(request, id):
    animais = Animal.objects.get(id=id)

    return render(request, "update.html", {"animais": animais})

def atualizar(request, id):
    animais = Animal.objects.get(id=id)

    nome = request.POST.get("nome")
    animais.nome = nome

    especie = request.POST.get("especie")
    animais.especie = especie

    nome_dono = request.POST.get("nome_dono")
    animais.nome_dono = nome_dono

    telefone = request.POST.get("telefone")
    animais.telefone = telefone

    animais.save()

    return redirect(home)

def deletar(request, id):
    animais = Animal.objects.get(id=id)
    animais.delete()

    return redirect(home)