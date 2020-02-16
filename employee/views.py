from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from users.views import signup
from employee.forms import *
from employee.db_ops import *
from indexapp.constants import INDUSTRY_CATEGORIES, EMPLOYMENT_TYPES, COMPANY_SIZES


@login_required()
def edit_profile(request):
    profile = EmployeeProfile.objects.get(user=request.user)
    profile_pic = profile.profile_pic.url
    form = UpdateProfileForm(instance=profile)
    form_education = UpdateEducation()
    form_experience = UpdateExperience()
    form_proficiency = UpdateEmployeeProficiency()
    form_resume = UpdateResume()
    form_language = UpdateLanguage()

    values = {
        'education': get_education(request.user),
        'experience': get_experience(request.user),
        'languages': get_languages(request.user),
    }

    context = {
        'form': form,
        'form_language': form_language,
        'form_resume': form_resume,
        'form_experience': form_experience,
        'form_education': form_education,
        'form_proficiency': form_proficiency,
        'pic': profile_pic,
        'values': values,
        'industries': INDUSTRY_CATEGORIES,
        'employment_types': EMPLOYMENT_TYPES,
        'company_sizes': COMPANY_SIZES
    }

    return render(request, "edit_profile.html", context)


@login_required()
def update_profile(request):
    if request.method == 'POST':
        try:
            profile = EmployeeProfile.objects.get(user=request.user)
        except EmployeeProfile.DoesNotExist:
            profile = None

        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save(commit=False)
            form.email = request.user.email
            form.save()
            return redirect('employee-edit-profile')

    return HttpResponse('error')


@login_required()
def update_education(request):
    if request.method == 'POST':
        instance = EmployeeEducation(user=request.user)
        form = UpdateEducation(request.POST, instance=instance)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee-edit-profile')
        else:
            print(form.errors)
            return render(request, 'profile.html', {'education_error': form.errors})

    return HttpResponse('error')


@login_required()
def update_experience(request):
    if request.method == 'POST':
        instance = EmployeeExperience(user=request.user)
        form = UpdateExperience(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('employee-edit-profile')
        else:
            print(form.errors)
            return render(request, 'profile.html', {'experience_error': form.errors})

    return HttpResponse('error')


@login_required()
def update_resume(request):
    if request.method == 'POST':
        instance = EmployeeResume(user=request.user)
        form = UpdateResume(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('employee-edit-profile')

    return HttpResponse('error')


@login_required()
def update_language(request):
    if request.method == 'POST':
        instance = EmployeeLanguage(user=request.user)
        form = UpdateLanguage(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('employee-edit-profile')

    return HttpResponse('error')


@login_required()
def view_profile(request):

    return render(request, "view-profile.html", {'name': request.user.email})


@login_required()
def my_jobs(request):
    return render(request, "applied_jobs.html")


def signup_page(request):
    form = SignUpForm()
    return render(request, "signup.html", {'form': form})


def signup_form(request):
    error = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            password_verification = form.clean_password()

            if password_verification is None:
                error = True
                return render(request, "signup.html", {'form': form, 'error': error})
            else:
                user = signup(request=request,
                              email=form.cleaned_data['email'],
                              user_type='employee',
                              password=password_verification)
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('signin')
        form = SignUpForm()
        return render(request, "signup.html", {'form': form, 'error': error})


@login_required()
def delete(request):
    lang = request.GET.get('language', None)
    edu = request.GET.get('education', None)
    job = request.GET.get('experience', None)
    status = None

    if request.user.is_anonymous:
        return JsonResponse({'status': 0})

    if request.is_ajax():
        if request.user.is_anonymous:
            return JsonResponse({'status': 0})
        if request.is_ajax():
            if lang:
                lang = EmployeeLanguage.objects.get(id=lang, user=request.user)
                lang.delete()
            elif edu:
                edu = EmployeeEducation.objects.get(id=edu, user=request.user)
                edu.delete()
            elif job:
                job = EmployeeExperience.objects.get(id=job, user=request.user)
                job.delete()
            return JsonResponse({'status': 1})
