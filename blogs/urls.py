from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogpost, name='blogpost'),
    path('new_area/', views.new_area, name='new_area'),

]