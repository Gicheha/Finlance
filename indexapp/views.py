from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from users.models import User
from indexapp.db_ops import *
from indexapp.constants import INDUSTRY_CATEGORIES, EMPLOYMENT_TYPES


def index(request):
    jobs = paginate(get_jobs(), request.GET.get('page', 1))
    context = {'jobs': jobs, 'categories': INDUSTRY_CATEGORIES[1:]}
    return render(request, "index.html", context=context)


def jobs(request):
    jobs = paginate(get_jobs(), request.GET.get('page', 1))
    context = {'jobs': jobs, 'categories': INDUSTRY_CATEGORIES[1:]}
    return render(request, "job-listings.html", context)


def single_job(request, slug):
    job = get_job(slug)
    context = {'job': job, 'categories': INDUSTRY_CATEGORIES[1:]}
    return render(request, "job-single.html", context=context)


def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).exists()
        if user:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if(user.user_type == 'employee'):
                    return redirect('employee-edit-profile')
                if(user.user_type == 'customer'):
                    return redirect('customer_home')
            else:
                return HttpResponse(
                    "Your account has not been activated, kindly check your email for the verification code")
        else:
            return HttpResponse("You do not have an account, kindly register to have an account with us")

    return render(request, "signin.html")


def blog(request):
    return render(request, 'blog.html')


def logout_view(request):
    print(request.user.is_anonymous)
    logout(request)
    return redirect('index')


def contacts(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")

