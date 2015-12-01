from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import *


def dogs_index(request):
    dogs_list = Dog.objects.order_by('-last_updated')
    context = RequestContext(request, {'dogs_list': dogs_list})
    return render(request, 'app/dogs_index.html', context)


def dog_details(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    context = RequestContext(request, {'dog': dog})
    return render(request, 'app/dog_details.html', context)


def dogs_4_adoption(request):
    context = RequestContext(request, {'dog': 'dog'})
    return render(request, 'app/dogs_4_adoption.html', context)


def dogs_list(request):
    dog_size = request.GET.get("dog_size", "")
    return HttpResponse("%s" % dog_size)
