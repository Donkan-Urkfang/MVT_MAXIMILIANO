from django.shortcuts import render
from model.models import familiares


def listaFamiliares(request):
    familiar1 = familiares(numero=1, nombre="Paula", apellido="Saler", fecha='1972-02-07')
    familiar1.save()
    familiar2 = familiares(numero=2, nombre="Pedro", apellido="Bandargia", fecha='1969-07-25')
    familiar2.save()
    familiar3 = familiares(numero=3, nombre="Gaston", apellido="Bandargia", fecha='1948-11-01')
    familiar3.save()
    contexto = {
        "familiar1":familiar1,
        "familiar2":familiar2,
        "familiar3":familiar3
    }

    return render(request, "familiares.html", contexto)