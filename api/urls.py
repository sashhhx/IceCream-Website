from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    # path('<int:pk>', views.contact_detail, name = 'info'),
    path('', views.contact_detail, name = 'info'),
    path('all', views.contact_detail_list, name='infolist')
]