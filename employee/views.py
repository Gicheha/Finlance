from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from users.views import SignUpView
from employee.forms import *
from employee.db_ops import *
from indexapp.constants import INDUSTRY_CATEGORIES, EMPLOYMENT_TYPES, COMPANY_SIZES


@login_required()
def edit_profile(request):
    profile = EmployeeProfile.objects.get(user=request.user)
    profile_pic = profile.profile_pic.url
    form = UpdateProfileForm(instance=profile)
    form_education = UpdateEducation()
    form_proficiency = UpdateEmployeeProficiency()
    form_experience = UpdateExperience()
    form_resume = UpdateResume(instance=EmployeeResume.objects.filter(user=request.user).last())
    form_language = UpdateLanguage()
    values = {'education': get_education(request.user),
              'experience': get_experience(request.user),
              'languages': get_languages(request.user)}
    context = {'form': form,
               'form_proficiency': form_proficiency,
               'form_language': form_language,
               'form_resume': form_resume,
               'values': values,
               'form_experience': form_experience,
               'form_education': form_education,
               'pic': profile_pic,
               'industries': INDUSTRY_CATEGORIES,
               'employment_types': EMPLOYMENT_TYPES,
               'company_sizes': COMPANY_SIZES
               }
    return render(request, "templates/profile.html", context)


@login_required()
def update_profile(request):
    if request.method == 'POST':
        profile = EmployeeProfile.objects.get(user=request.user)
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

        if form.is_valid():
            form.save()
            return redirect('update-education')

    return HttpResponse('error')


@login_required()
def update_experience(request):
    if request.method == 'POST':
        instance = EmployeeExperience(user=request.user)
        form = UpdateExperience(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('update-experience')

    return HttpResponse('error')


@login_required()
def update_resume(request):
    if request.method == 'POST':
        instance, created = UpdateResume.objects.get_or_create(user = request.user)
        form = UpdateResume(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('update-resume')

    return HttpResponse('error')


@login_required()
def update_language(request):
    if request.method == 'POST':
        instance = EmployeeLanguage(user=request.user)
        form = UpdateLanguage(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('update-language')

    return HttpResponse('error')


@login_required()
def view_profile(request):
    return render(request, "templates/view-user-profile.html")


@login_required()
def my_jobs(request):
    return render(request, "templates/user-jobs.html")


def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            password_verification = form.clean_password()

            if password_verification:
                return render(request, "templates/employee-signup.html", {'form': form})
            else:
                user = SignUpView(request=request,
                                  email=form.cleaned_data['email'],
                                  user_type='employer',
                                  password=password_verification)
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('index')
        form = SignUpForm()
        return render(request, "templates/employer-signup.html", {'form': form})


def signup_employee(request):
    form = SignUpForm()
    return render(request, "templates/job-seeker-signup.html", {'form': form})


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
                lang =  EmployeeLanguage.objects.get(id=lang, user=request.user)
                lang.delete()
            elif edu:
                edu = EmployeeEducation.objects.get(id=edu, user=request.user)
                edu.delete()
            elif job:
                job = EmployeeExperience.objects.get(id=job, user=request.user)
                job.delete()
            return JsonResponse({'status': 1})