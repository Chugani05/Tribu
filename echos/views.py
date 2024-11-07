from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import AddEchoForm
from .models import Echo


@login_required
def echo_list(request: HttpRequest) -> HttpResponse:
    echos = Echo.objects.all()
    return render(request, 'echos/echo_list.html', dict(echos=echos))


@login_required
def add_echo(request):
    if request.method == 'POST':
        if (form := AddEchoForm(request.POST)).is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            echo.save()
            return redirect('echos:echo-list')
    else:
        form = AddEchoForm()
    return render(request, 'echos/add_echo.html', dict(form=form))


@login_required
def echo_detail(request: HttpRequest, echo_pk: str) -> HttpResponse:
    echo = Echo.objects.get(id=echo_pk)
    return render(request, 'echos/echo_detail.html', dict(echo=echo))


@login_required
def edit_echo(request, echo_pk):
    task = Echo.objects.get(id=echo_pk)
    if request.method == 'POST':
        if (form := AddEchoForm(request.POST, instance=echo)).is_valid():
            echo = form.save(commit=False)
            echo.id = echo_pk
            echo.save()
            return redirect('echos:echo-list')
    else:
        form = AddEchoForm(instance=task)
    return render(request, 'echos/edit_echo.html', dict(form=form, echo=echo))


@login_required
def delete_echo(request, echo_pk):
    echo = Echo.objects.get(id=echo_pk)
    echo.delete()
    return render(request, 'echos/delete_echo.html', dict(echo=echo))


@login_required
def echo_waves(request: HttpRequest) -> HttpResponse:
    pass


def add_wave(request):
    wave = form.save(commit=False)
    wave.user = request.user
    wave.echo = echo
    wave.save
    pass