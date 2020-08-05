from django.urls import path, include
from . import views
from .views import database, company_api

urlpatterns = [
    # path('', views.employee, name='employee'),
    path('database/', database, name= 'database'),
    path('company_api/', company_api , name='company_api'),
    ]