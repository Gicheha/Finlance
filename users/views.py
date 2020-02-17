from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from users.models import User


def signup(request, email, user_type, password):
    user = User.objects.create_user(email, user_type, password)
    user.is_active = True
    user.save()
    return user

def logout_view(request):
    print(request.user.is_anonymous)
    logout(request)
    return redirect('index')

