from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from indexapp.constants import *

from users.models import User
from employee.models import *

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=30)
    contact_person_name = models.CharField(max_length=64)
    company_size = models.CharField(max_length=50, choices=COMPANY_SIZES)
    country = models.CharField(max_length=64, default='Kenya')
    business_description = RichTextField()
    tax_details = models.TextField

    def __str__(self):
        return self.business_name
    
    def __unicode__(self):
        return self.id


class Job(models.Model):
    hiring_organization = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=164)
    slug = AutoSlugField(populate_from='title', unique=True, max_length=200, blank=True, null=True)
    description = RichTextField()
    employment_type = models.CharField(max_length=64, choices=EMPLOYMENT_TYPES)
    experience = models.IntegerField(null=True, blank=True)
    job_location = models.CharField(max_length=64, default='Nairobi')
    date_posted = models.DateField(default=timezone.now)
    valid_through = models.DateField()
    education_level = models.CharField(choices=DEGREE_LEVEL, max_length=200, default='DEGREE_TYPE_UNSPECIFIED')
    job_level = models.CharField(choices=JOB_LEVEL, max_length=200, default='JOB_LEVEL_UNSPECIFIED')
    category = models.CharField(max_length=200, choices=INDUSTRY_CATEGORIES)
    max_salary = models.IntegerField(null=True, blank=True)
    min_salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class ShortList(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)


