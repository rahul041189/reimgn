from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)/$', views.show_property),
    url(r'terms_conditions/', views.terms),
    url(r'privacy/', views.privacy),
]
