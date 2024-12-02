from django.urls import path
from . import views

app_name = 'programs'

urlpatterns = [
    path('', views.programs_list, name='programs_list'),
    path('programs/create', views.programs_create, name='programs_create'),
]