from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.home, name ='home'),
    url(r'^search/', views.search_category, name='search_category'),
    url(r'^location/', views.filter_by_location, name='filter_by_location'),
    url(r'^image/', views.get_image_id, name='get_image_id'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)