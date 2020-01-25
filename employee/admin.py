from django.contrib import admin

from employee.models import  *

# Register your models here.
admin.site.register(EmployeeEducation)
admin.site.register(EmployeeExperience)
admin.site.register(EmployeeProfile)
admin.site.register(EmployeeResume)
admin.site.register(EmployeeLanguage)
