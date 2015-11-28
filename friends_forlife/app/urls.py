from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^dogs-index', views.dogs_index, name="dogs_index"),
    url(r'^dog-details/(?P<dog_id>[0-9]+)', views.dog_details, name="dog_details")
]