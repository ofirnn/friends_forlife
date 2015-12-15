from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import *
import datetime

ALL_STRING ="All"


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


def house_registration(request):
    context = RequestContext(request, {'dog': 'dog'})
    return render(request, 'app/house_registration.html', context)


def house_register(request):
    req_owner_name = request.GET.get("owner_name", "N/A")
    req_owner_phone = request.GET.get("owner_phone", "N/A")
    req_owner_email = request.GET.get("owner_email", "N/A")
    req_owner_city = request.GET.get("owner_city", "N/A")
    req_address = request.GET.get("address", "N/A")
    req_capaticy = request.GET.get("capacity", "N/A")

    new_house = DogHouse(owner_name=req_owner_name, owner_phone=req_owner_phone,
                         owner_email=req_owner_email, owner_city=req_owner_city, address=req_address,
                         capacity=req_capaticy)
    new_house.save()

    context = RequestContext(request, {'dog_house': new_house})

    return render(request, "app/success_house_registration.html", context)


def dog_insretion(request):
    context = RequestContext(request, {'dog': 'dog'})
    return render(request, 'app/dog_insert.html', context)


def dog_insert(request):
    req_name = request.GET.get("name")
    req_description = request.GET.get("description", "N/A")
    req_color = request.GET.get("color", "N/A")
    req_age = request.GET.get("age")
    req_gender = request.GET.get("gender")
    req_status = request.GET.get("status")
    req_chip_id = request.GET.get("chip_id", "N/A")
    req_size = request.GET.get("size", "N/A")
    req_type_name = request.GET.get("type_name", "N/A")

    req_picture = request.GET.get("picture")

    characteristics = request.GET.getlist("Characteristics[]", [])

    req_children_friendly = False
    req_suitable_for_allergic = False
    req_habituated_for_needs = False
    req_is_casrated = False

    if "childrens_friendly" in characteristics:
        req_children_friendly = True
    if "suitable_for_allergic" in characteristics:
        req_suitable_for_allergic = True
    if "habituated_for_needs" in characteristics:
        req_habituated_for_needs = True
    if "is_castrated" in characteristics:
        req_is_casrated = True

    last_updated = datetime.datetime.now()

    dog = Dog(name=req_name, description=req_description, color=req_color,
              age=req_age, is_adopted=False, is_castrated=req_is_casrated,
              is_educated=req_habituated_for_needs, gender=req_gender,
              status=req_status, last_updated=last_updated, picture=req_picture,
              chip_id=req_chip_id, size=req_size, type_name=req_type_name,
              is_hypoallergenic=req_suitable_for_allergic,
              is_children_friendly=req_children_friendly)

    dog.save()

    context = RequestContext(request, {'dog': dog})
    return render(request, "app/success_dog_insertion.html", context)

def dogs_list(request):
    #Parameters : gender, dog_size, dog_age, dog_breed, dog_color
    # childrens_friendly, suitable_for_allergic , habituated_for_needs

    req_gender = request.GET.get("gender", ALL_STRING)
    req_size = request.GET.get("dog_size", ALL_STRING)
    req_age = request.GET.get("dog_age", ALL_STRING)
    req_breed = request.GET.get("dog_breed", ALL_STRING)
    req_color = request.GET.get("dog_color", ALL_STRING)

    characteristics = request.GET.getlist("Characteristics[]", [])

    req_children_friendly = False
    req_suitable_for_allergic = False
    req_habituated_for_needs = False

    if "childrens_friendly" in characteristics:
        req_children_friendly = True
    if "suitable_for_allergic" in characteristics:
        req_suitable_for_allergic = True
    if "habituated_for_needs" in characteristics:
        req_habituated_for_needs = True
    print req_gender

    dogs = Dog.objects.all()

    print dogs
    if req_gender != ALL_STRING:
        print "Filtering Gender"
        dogs = dogs.filter(Q(gender=req_gender))
    if req_size != ALL_STRING:
        print "Filtering Size"
        dogs = dogs.filter(Q(size=req_size))
    if req_age != ALL_STRING:
        print "Filtering Age"
        dogs = dogs.filter(Q(age=req_age))
    if req_breed != ALL_STRING:
        print "Filtering breed"
        dogs = dogs.filter(Q(type_name=req_breed))
    if req_color != ALL_STRING:
        print "Filtering color"
        dogs = dogs.filter(Q(color=req_color))

    if req_children_friendly:
        print "Filtering childen_friendly"
        dogs = dogs.filter(Q(is_children_friendly=True))
    if req_habituated_for_needs:
        print "Filtering educated"
        dogs = dogs.filter(Q(is_educated=True))
    if req_suitable_for_allergic:
        print "Filtering hypoallergenic"
        dogs = dogs.filter(Q(is_hypoallergenic=True))

    dogs = dogs.order_by('-last_updated')
    context = RequestContext(request, {'dogs_list': dogs})
    return render(request, 'app/dogs_list.html', context)


def index(request):
    context = RequestContext(request, {'dog': 'dog'})
    return render(request, 'app/index.html', context)