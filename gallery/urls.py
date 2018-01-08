from django.conf.urls import url
from .views import view_images,category

urlpatterns = [
    url(r'^$',view_images,name='gallery'),
    url(r'^category/(?P<slug>[\w-]+)/$',category, name='view_category')
]