from django.urls import path
from employee.views import *

urlpatterns = [
    path('edit-profile', edit_profile, name='employee-edit-profile'),
    path('jobs/', my_jobs, name='my-jobs'),
    path('signup/', signup_form, name='employee-signup'),
    path('view-profile', view_profile, name='view-profile'),
    path('signup-form/', signup_form, name='employee-signup-form'),
    path('update-profile', update_profile, name='update-profile'),
    path('update-education', update_education, name='update-education'),
    path('update-experience', update_experience, name='update-experience'),
    path('update-resume/', update_resume, name='update-resume'),
    path('update-language/', update_language, name='update-language'),
    path('api/delete/', delete, name='delete-item')
]
