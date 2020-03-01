from django.urls import path
from customer.views import *

urlpatterns = [
    path('dashboard/', customer_home, name='dashboard'),
    path('new-job/', new_job, name='new-job'),
    path('myjobs/', myjobs, name='myjobs'),
    path('job/<str:slug>',view_job,name='job-post'),
    path('update-employer/', update_customer, name='update-employer'),
    path('signup/', signup_employer, name='signup-employer'),
    path('signup-form/', signup_form, name='signup-employer-form')
]