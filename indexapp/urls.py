from django.urls import path, re_path
from django.conf.urls import url
from indexapp.views import *

urlpatterns = [
    path('signin/', sign_in, name='signin'),
    url(r'^$', index, name='index'),
    path('blog/', blog, name='blog'),
    path('logout/', logout_view, name='logout'),
    path('contacts/', contacts, name='contacts'),
    path('jobs/', jobs, name='jobs'),
    path('job/<str:slug>', single_job, name='job-post'),
    path('about/', about, name='about'),
]
