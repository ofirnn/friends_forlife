from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^dogs-index', views.dogs_index, name="dogs_index"),
    url(r'^dogs_index', views.dogs_index, name="dogs_index"),
    url(r'^dogs_list', views.dogs_list, name="dogs_list"),
    #url(r'^dog-details/(?P<dog_id>[0-9]+)', views.dog_details, name="dog_details"),
    url(r'^dogs_4_adoption', views.dogs_4_adoption, name="dogs_4_adoption"),
    url(r'^house_registration', views.house_registration, name="house_registration"),
    url(r'^house_register', views.house_register, name="house_register_endpoint"),
    url(r'^dogstaying_add', views.dogstaying_add, name="dogstaying_add"),
    url(r'^dogstay_addition', views.dogstaying_addition, name="dogstaying_addition_endpoint"),
    url(r'^contact_us', views.contact_us, name="contact_us"),
    url(r'^donate', views.donation, name="donation_page"),
    url(r'^dog_insertion', views.dog_insertion, name="dog_insertion"),
    url(r'^dog_insert', views.dog_insert, name="dog_insert_endpoint"),
    url(r'^dog_updation', views.dog_updation, name="dog_updation"),
    url(r'^dog_update', views.dog_update, name="dog_update_endpoint"),

    url(r'^index', views.index),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
