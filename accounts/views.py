from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, SignupForm


def user_login(request):
    if request.method == 'POST':
        if (form := LoginForm(request.POST)).is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if user := authenticate(request, username=username, password=password):
                login(request, user)
                return redirect('echos:echo-list')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', dict(form=form))


def user_logout(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def user_signup(request):
    if request.method == 'POST':
        if (form := SignupForm(request.POST)).is_valid():
            user = form.save()
            login(request, user)
            return redirect('echos:echo-list')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', dict(form=form))
