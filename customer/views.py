from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from users.views import signup
from customer.forms import JobForm,SignUpForm,UpdateCustomer
from customer.models import *

@login_required()
def customer_home(request):
    employer = Customer.objects.last()
    form = UpdateCustomer(instance=employer)
    return render(request, "clientpage.html")


@login_required()
def update_customer(request):
    if request.method == 'POST':
        form = UpdateCustomer(request.POST, instance=Customer.objects.last())

        if form.is_valid():
            form.save()
            print('success')
            return redirect('/employer/dashboard/#nav-profile')
    return redirect('dashboard')


@login_required()
def new_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myjobs')
        return render(request, "post_job.html", {'form': form})
    form = JobForm()
    return render(request, "post_job.html", {'form': form})
\

def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            password_verification = form.clean_password()

            if password_verification:
                return render(request, "templates/employer-signup.html", {'form': form})
            else:
                user = signup(request=request, email=form.cleaned_data['email'],
                                  user_type='employer',
                                  password=password_verification)
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('index')

    form = SignUpForm()
    return render(request, "templates/employer-signup.html", {'form': form})


@login_required
def myjobs(request):
    customer = Customer.objects.get(user = request.user)
    jobs = Job.objects.filter(hiring_organization = customer)
    return render(request, 'myjobs.html', {'jobs' : jobs})


def view_job(request, slug):
    job =Job.objects.get(slug = slug)
    return render(request, 'job.html', {'job': job})


def signup_employer(request):
    form = SignUpForm()
    return render(request, "templates/employer-signup.html", {'form': form})
