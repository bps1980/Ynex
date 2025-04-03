from . import views
from django.urls import path

appname = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
]