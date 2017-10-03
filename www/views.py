# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person
from .forms import PersonForm


# Create your views here.

def index(request):
    people = Person.objects.all()
    form = PersonForm()
    return render(request, 'index.html', {'people':people, 'form': form})


def elim_directorio(request):
    people = Person.objects.all()
    form = PersonForm()
    return render(request, 'elim-directorio.html', {'people':people, 'form': form})

def detail(request, person_id):
    person = Person.objects.get(id=person_id)
    return render(request, 'details.html', {'person':person})


def post_person(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        person = Person(name = form.cleaned_data['name'],
                            email = form.cleaned_data['email'],
                            title = form.cleaned_data['title'],
                            image = form.cleaned_data['image'],
                            mapa = form.cleaned_data['mapa']
                            )
        person.save()

    return HttpResponseRedirect('/elim-directorio')


def predicas_elim(request):
    predica_actual = 'https://www.youtube.com/watch?v=2q7gvS09KO4'
    return render(request, 'predicas.html', {'predicas_actual': predica_actual})

def quienes_somos(request):
    return render(request, 'quienes-somos.html')


def elim_tv(request):
    return render(request, 'elim-tv.html')

def elim_radio(request):
    return render(request, 'elim-radio.html')