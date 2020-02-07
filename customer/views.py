from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.views import signup
from customer.forms import *

@login_required()
def customer_home(request):
    employer = Customer.objects.last()
    form = UpdateCustomer(instance=employer)
    return render(request, "templates/employer-dashboard.html")


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
    hiring_organization = Customer.objects.last()
    hiring_organization.id = 22
    hiring_organization.pk = 22

    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.hiring_organization = hiring_organization
            form.save()
        return render(request, "templates/new-job.html", {'form': form})
    form = JobForm()
    return render(request, "templates/new-job.html", {'form': form})


def view_job(request, slug):
    return render(request, "templates/view-job.html")


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


def signup_employer(request):
    form = SignUpForm()
    return render(request, "templates/employer-signup.html", {'form': form})
