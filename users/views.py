from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import EditProfileForm
from .models import Profile


@login_required
def user_list(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    return render(request, 'users/user_list.html', dict(users=users))


@login_required
def my_profile(request: HttpRequest) -> HttpResponse:
    return redirect('users:user-detail', username=request.user)


@login_required
def user_detail(request: HttpRequest, username: str) -> HttpResponse:
    consumer = User.objects.get(username=username)
    echos = consumer.echos.all()
    last_echos = echos[:5]
    return render(
        request,
        'users/user_detail.html',
        dict(consumer=consumer, echos=last_echos, quantity=len(echos)),
    )


@login_required
def edit_profile(request: HttpRequest, username: str) -> HttpResponse:
    consumer = User.objects.get(username=username)
    consumer_profile = consumer.profile
    if consumer != request.user:
        return HttpResponseForbidden('Error 403 - Forbidden')
    if request.method == 'POST':
        if (form := EditProfileForm(request.POST, request.FILES, instance=consumer_profile)).is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('users:user-detail', username)
    else:
        form = EditProfileForm(instance=consumer_profile)
    return render(request, 'users/edit_profile.html', dict(form=form))


@login_required
def user_echos(request: HttpRequest, username: str) -> HttpResponse:
    consumer = User.objects.get(username=username)
    echos = consumer.echos.all()
    return render(request, 'users/user_echos.html', dict(consumer=consumer, echos=echos))
