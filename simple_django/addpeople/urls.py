from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('postperson/', views.postPerson, name='postPerson'),
    path('getpeople/<int:id>', views.getPeople, name ='getPeople')
]