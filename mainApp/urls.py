from django.urls import path, include
from mainApp.views import *

urlpatterns = [
    path('home/', home_page, name='home'),
]
