from users.models import User


def signup(request, email, user_type, password):
    user = User.objects.create_user(email, user_type, password)
    user.is_active = True
    user.save()
    return user

