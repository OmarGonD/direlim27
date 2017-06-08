# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Person

# Create your views here.

def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people':people})
