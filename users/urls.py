from django.urls import path
from users.views import *

urlpatterns = [
    path('logout/', logout_view, name='logout')
]