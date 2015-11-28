from django.db import models
import json
# Create your models here.


# class DogType(models.Model):
#     name = models.CharField(max_length=200, help_text="The name of the Dog-type")
#     is_hypoallergenic = models.BooleanField(default=False)
#     is_children_friendly = models.BooleanField(default=True)
#     description = models.TextField()


class DogHouse(models.Model):
    owner_name = models.CharField(max_length=200, help_text="Name of doghouse owner")
    owner_phone = models.CharField(max_length=200, help_text="Phone Number of owner")
    owner_email = models.EmailField(help_text="Email of doghouse owner")
    owner_city = models.CharField(max_length=50)
    address = models.CharField(max_length=500, help_text="Full-Address Of DogHouse")
    capacity = models.IntegerField(help_text="Maximum dogs capacity")


class DogStaying(models.Model):
    house = models.ForeignKey(DogHouse)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(null=True, blank=True)


class Dog(models.Model):
    name = models.CharField(max_length=200, help_text="The name of the Dog")

    description = models.TextField()
    color = models.CharField(max_length=100)
    birth_date = models.DateField()

    is_adopted = models.BooleanField(default=False)
    is_castrated = models.BooleanField(default=False)
    is_educated = models.BooleanField(default=False)

    status = models.CharField(max_length=50, help_text="State Name - In-Adoption / In-House / Treatment ")
    last_updated = models.DateTimeField(auto_created=True)
    picture = models.ImageField(null=True, blank=True)
    chip_id = models.CharField(max_length=200, help_text="IL chip-id")

    type_name = models.CharField(max_length=200, null=True, help_text="The name of the Dog-type")
    is_hypoallergenic = models.BooleanField(default=False)
    is_children_friendly = models.BooleanField(default=True)

    stayings = models.ManyToManyField(DogStaying)

    def __str__(self):
        output = dict()

        output["name"] = self.name
        output["type_name"] = self.type_name
        return json.dumps(output)

class AdoptionDay(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(null=True, blank=True)


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    ils_value = models.FloatField()
    image = models.ImageField()


class BasketItem(models.Model):
    item = models.ForeignKey(Item)
    quantity = models.IntegerField(default=1)


class DonationBasket(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    items = models.ManyToManyField(BasketItem)
    creation_date = models.DateTimeField(auto_now=True)
