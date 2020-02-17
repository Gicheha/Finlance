from employee.models import *


def get_education(user):
    return EmployeeEducation.objects.filter(user=user)


def get_experience(user):
    return EmployeeExperience.objects.filter(user=user)


def get_skills(user):
    return EmployeeProficiency.objects.filter(user=user)


def get_languages(user):
    return EmployeeLanguage.objects.filter(user=user)

def get_resume(user):
    return EmployeeResume.objects.filter(user=user)