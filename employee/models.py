from django.db import models
from users.models import User
from indexapp.constants import DEGREE_LEVEL, INDUSTRY_CATEGORIES, EMPLOYMENT_TYPES, COMPANY_SIZES, LANGUAGES
from indexapp.constants import PROFICIENCY, STATUS


# Create your models here.
class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile-pics', blank=True, default='profile-pics/profile.png')
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    id_number = models.CharField(max_length=8, unique=True)
    status = models.CharField(max_length=32, choices=STATUS)
    is_suspended = models.BooleanField(default=False)
    city = models.CharField(max_length=64, blank=True)
    country = models.CharField(max_length=30, default='Kenya', blank=True)

    def __str__(self):
        return self.first_name + self.last_name


class EmployeeEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=500)
    study_field = models.CharField(max_length=500)
    certification = models.CharField(max_length=500, choices=DEGREE_LEVEL)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.institution


class EmployeeProficiency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=32)
    proficiency = models.CharField(max_length=63, choices=PROFICIENCY)
    certified = models.BooleanField

    def __str__(self):
        return self.skill


class EmployeeExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=500)
    company_homepage = models.URLField(blank=True)
    job_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPES)
    company_size = models.CharField(max_length=200, blank=True, choices=COMPANY_SIZES)
    industry = models.CharField(max_length=500, choices=INDUSTRY_CATEGORIES)
    position = models.CharField(max_length=500)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current_job = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.company + self.position


class EmployeeLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, choices=LANGUAGES)
    proficiency = models.CharField(max_length=50, choices=PROFICIENCY)

    def __str__(self):
        return self.language


class EmployeeResume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cv')
    cover_letter = models.TextField()

    def __str__(self):
        return self.cover_letter
