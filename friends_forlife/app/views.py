from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from lxml import html
import requests
from models import *
import datetime

import _ssl
_ssl.PROTOCOL_SSLv23 = _ssl.PROTOCOL_TLSv1

ALL_STRING = "All"

CHIP_INFO_BASE_URL = "https://klav.im/results/"



def login_endpoint(request):
    username = request.POST.get("usermail")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        print user
        login(request, user)
        return index(request)
    else:
        return HttpResponse("Incorrect password")


@login_required()
def logout_endpoint(request):
    logout(request)
    return index(request)


def chip_search(request):
    context = RequestContext(request, {'dog': 'dog'})
    return render(request, 'app/chip_search.html', context)


def chip_info(request):
    findstr = request.GET.get("chip_id")

    page = requests.get("%s%s" % (CHIP_INFO_BASE_URL, findstr))
    tree = html.fromstring(page.content)

    dog_chip_info = dict()

    name = tree.xpath('//*[@id="results"]/ul/li[1]/div/text()')
    if len(name) == 0:
        dog_chip_info['name'] = "None"
    else:
        dog_chip_info['name'] = name[0]
        dog_chip_info['type_name'] = tree.xpath('//*[@id="results"]/ul/li[3]/div/div')[0].text_content()
        dog_chip_info['birth_date'] = tree.xpath('//*[@id="results"]/ul/li[7]/div/div')[0].text_content()
        dog_chip_info['last_kalevet'] = tree.xpath('//*[@id="results"]/ul/li[9]/div/div')[0].text_content()
        dog_chip_info['is_castrated'] = tree.xpath('//*[@id="results"]/ul/li[5]/div/div')[0].text_content()
        dog_chip_info['owner_name'] = tree.xpath('//*[@id="results"]/ul/li[10]/div/div/a')[0].text_content()
        dog_chip_info['owner_phone'] = tree.xpath('//*[@id="results"]/ul/li[11]/div/div[1]')[0].text_content()
        dog_chip_info['color'] = tree.xpath('//*[@id="results"]/ul/li[4]/div/div')[0].text_content()

        address = ""
        for item in tree.xpath('//*[@id="results"]/ul/li[12]/div/div'):
            address += item.text_content()
            address += " "

        dog_chip_info['owner_address'] = address

    print dog_chip_info
    context = RequestContext(request, {'dog_chip_info': dog_chip_info})
    return render(request, 'app/chip_info.html', context)


@login_required()
def dog_delete(request):
    id = request.GET.get("id")
    dog = Dog.objects.get(id=id)
    dog.delete()

    return dogs_index(request)


@login_required()
def doghouse_delete(request):
    id = request.GET.get("id")
    dog_house = DogHouse.objects.get(id=id)
    dog_house.delete()

    return doghouse_index(request)


@login_required()
def dogs_index(request):
    dogs_list = Dog.objects.order_by('-last_updated')
    context = RequestContext(request, {'dogs_list': dogs_list})
    return render(request, 'app/dogs_index.html', context)


@login_required()
def doghouse_index(request):
    houses_list = DogHouse.objects.all()
    context = RequestContext(request, {'houses_list': houses_list})
    return render(request, 'app/doghouse_index.html', context)


def dogs_4_adoption(request):
    dogs_list = Dog.objects.order_by('-last_updated')
    context = RequestContext(request, {'dogs_list': dogs_list})
    return render(request, 'app/dogs_4_adoption.html', context)


def house_registration(request):
    context = RequestContext(request, {'dog': 'dog'})
    return render(request, 'app/house_registration.html', context)


def house_register(request):
    req_owner_name = request.POST.get("owner_name", "N/A")
    req_owner_phone = request.POST.get("owner_phone", "N/A")
    req_owner_email = request.POST.get("owner_email", "N/A")
    req_owner_city = request.POST.get("owner_city", "N/A")
    req_address = request.POST.get("address", "N/A")
    req_capaticy = request.POST.get("capacity", "N/A")

    new_house = DogHouse(owner_name=req_owner_name, owner_phone=req_owner_phone,
                         owner_email=req_owner_email, owner_city=req_owner_city, address=req_address,
                         capacity=req_capaticy)
    new_house.save()
    print "New House born"
    context = RequestContext(request, {'dog_house': new_house})

    return render(request, "app/success_house_registration.html", context)


@login_required(login_url='/accounts/login/')
def dog_insertion(request):
    context = RequestContext(request, {'dog': 'dog'})
    return render(request, 'app/dog_insert.html', context)


@login_required(login_url='/accounts/login/')
def dog_insert(request):
    req_name = request.POST.get("name")
    req_description = request.POST.get("description", "N/A")
    req_color = request.POST.get("color", "N/A")
    req_age = request.POST.get("age")
    req_gender = request.POST.get("gender")
    req_status = request.POST.get("status")
    req_chip_id = request.POST.get("chip_id", "N/A")
    req_size = request.POST.get("size", "N/A")
    req_type_name = request.POST.get("type_name", "N/A")
    req_status = request.POST.get("status", "N/A")
    req_picture = request.FILES.get("picture")
    req_children_friendly = request.POST.get("is_children_friendly", False)
    print req_children_friendly
    req_suitable_for_allergic = request.POST.get("is_hypoallergenic", False)
    print req_suitable_for_allergic
    req_habituated_for_needs = request.POST.get("is_educated", False)
    print req_habituated_for_needs

    last_updated = datetime.datetime.now()

    dog = Dog(name=req_name, description=req_description, color=req_color,
              age=req_age, is_adopted=False,
              is_educated=req_habituated_for_needs, gender=req_gender,
              status=req_status, last_updated=last_updated, picture=req_picture,
              chip_id=req_chip_id, size=req_size, type_name=req_type_name,
              is_hypoallergenic=req_suitable_for_allergic,
              is_children_friendly=req_children_friendly)

    dog.save()

    context = RequestContext(request, {'dog': dog})
    return render(request, "app/success_dog_insertion.html", context)


@login_required(login_url='/accounts/login/')
def dog_updation(request):
    req_id = request.GET.get("id")
    dog = Dog.objects.get(id=req_id)
    context = RequestContext(request, {'dog': dog})
    return render(request, 'app/dog_update.html', context)


@login_required(login_url='/accounts/login/')
def dog_update(request):
    req_id = request.POST.get("id")
    dog = Dog.objects.get(id=req_id)

    gender = request.POST.get("gender", dog.gender)
    size = request.POST.get("size", dog.size)
    age = request.POST.get("age", dog.age)
    type_name = request.POST.get("type", dog.type_name)
    color = request.POST.get("color", dog.color)

    picture = request.FILES.get("picture")
    print "REQ: %s" % request.FILES.keys()
    req_children_friendly = request.POST.get("is_children_friendly", False)
    print req_children_friendly
    req_suitable_for_allergic = request.POST.get("is_hypoallergenic", False)
    print req_suitable_for_allergic
    req_habituated_for_needs = request.POST.get("is_educated", False)
    print req_habituated_for_needs

    # Set Values
    dog.gender = gender
    dog.size = size
    dog.age = age
    dog.type_name = type_name
    dog.color = color
    print "dog picture is: %s" % picture
    if picture is not None:
        dog.picture = picture
    print "Now dog picture is: %s" % picture
    dog.is_children_friendly = req_children_friendly
    dog.is_hypoallergenic = req_suitable_for_allergic
    dog.is_educated = req_habituated_for_needs

    dog.save()

    context = RequestContext(request, {'dog': dog})
    return render(request, 'app/success_dog_updation.html', context)


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

def donation(request):
    basketks = DonationBasket.objects.all().order_by("-creation_date")
    context = RequestContext(request, {'donation_baskets': basketks})

    return render(request, 'app/donation_baskets.html', context)


def index(request):
    context = RequestContext(request, {'dog': 'dog'})
    return render(request, 'app/index.html', context)


@login_required()
def dogstaying_add(request):
    dog_id = request.GET.get("dog_id", None)
    house_id = request.GET.get("doghouse_id", None)

    if dog_id:
        houses_list = DogHouse.objects.all()
        context = RequestContext(request, {'id': dog_id, 'list': houses_list, 'src_type': 'dog'})
    elif house_id:
        dogs_list = Dog.objects.all().order_by("-last_updated")
        context = RequestContext(request, {'id': house_id, 'list': dogs_list, 'src_type': 'house'})

    return render(request, 'app/dogstaying_add.html', context)


@login_required()
def dogstaying_addition(request):
    dog_id = request.POST.get("dog_id", None)
    doghouse_id = request.POST.get("doghouse_id", None)
    start_date = request.POST.get("start_date", None)
    end_date = request.POST.get("end_date", None)

    dog = Dog.objects.get(id=dog_id)
    dog_house = DogHouse.objects.get(id=doghouse_id)

    dogstaying = DogStaying(house=dog_house, dog=dog, start_date=start_date, end_date=end_date)
    dogstaying.save()

    context = RequestContext(request, {'dogstaying': dogstaying})
    return render(request, 'app/success_dogstaying_add.html')


def contact_us(request):
    return