# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from .models import Carro
from .models import Fabricante
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index (request):
    todos_carro = Carro.objects.all()

    template = loader.get_template('carros/index.html')

    return HttpResponse(
        template.render({
            'carros': todos_carro
        }, request))



def detail (request, carro_id ):

    det_carro = get_object_or_404(Carro, pk=carro_id)
    return render(request, 'carros/detalhes.html', {'item': det_carro})


def fabri_list (request):

    todos_fab = Fabricante.objects.all()

    template = loader.get_template('carros/Fabricantes.html')

    return HttpResponse(
        template.render({
            'fabric': todos_fab
        }, request))


