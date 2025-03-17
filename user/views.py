from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from engine.models import User


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('module_list')
        else:
            return render(request, 'login.html', {
                'form': {'errors': True}
            })
    return render(request, 'login.html')


def login_as_guest(request):
    # Create or get guest user
    guest_user, created = User.objects.get_or_create(
        username='guest',
        defaults={
            'role': 'public',
            'password': 'unusablepassword'
        }
    )
    if created:
        guest_user.set_unusable_password()
        guest_user.save()

    # Log in the guest user
    login(request, guest_user)
    return redirect('module_list')

def user_logout(request):
    logout(request)
    return redirect('login')
