from django.conf.urls import url

from . import views
from django.conf.urls.static import static
from friends_forlife import settings

urlpatterns = [
    url(r'^dogs-index', views.dogs_index, name="dogs_index"),
    url(r'^dogs_list', views.dogs_list, name="dogs_list"),
    url(r'^dog-details/(?P<dog_id>[0-9]+)', views.dog_details, name="dog_details"),
    url(r'^dogs_4_adoption', views.dogs_4_adoption, name="dogs_4_adoption"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
