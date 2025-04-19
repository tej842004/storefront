from django.shortcuts import render
from django.db.models import Value, F, Func, Count
from django.db.models.functions import Concat
from store.models import Customer, Product, Collection


def say_hello(request):

    return render(request, 'hello.html', {'name': 'Prashant'})
