from django.urls import path, include
from . import views


urlpatterns = [
    path('1/', views.index,name='template1'),
    path('2/', views.second,name='template2'),
]
