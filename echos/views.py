from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render

from waves.forms import AddWaveForm

from .forms import AddEchoForm, EditEchoForm
from .models import Echo


@login_required
def echo_list(request: HttpRequest) -> HttpResponse:
    echos = Echo.objects.all()
    return render(request, 'echos/echo_list.html', dict(echos=echos))


@login_required
def add_echo(request: HttpRequest) -> HttpResponse:
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
def echo_detail(request: HttpRequest, echo_pk: int) -> HttpResponse:
    echo = Echo.objects.get(pk=echo_pk)
    waves = echo.waves.all()
    last_waves = waves[:5]
    return render(
        request, 'echos/echo_detail.html', dict(echo=echo, waves=last_waves, quantity=len(waves))
    )


@login_required
def edit_echo(request: HttpRequest, echo_pk: int) -> HttpResponse:
    echo = Echo.objects.get(pk=echo_pk)
    if echo.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
            echo = form.save(commit=False)
            echo.id = echo_pk
            echo.save()
            return redirect('echos:echo-list')
    else:
        form = EditEchoForm(instance=echo)
    return render(request, 'echos/edit_echo.html', dict(form=form, echo=echo))


@login_required
def delete_echo(request: HttpRequest, echo_pk: int) -> HttpResponse:
    echo = Echo.objects.get(pk=echo_pk)
    if echo.user != request.user:
        return HttpResponseForbidden()
    echo.delete()
    return render(request, 'echos/delete_echo.html', dict(echo=echo))


@login_required
def echo_waves(request: HttpRequest, echo_pk: int) -> HttpResponse:
    echo = Echo.objects.get(pk=echo_pk)
    waves = echo.waves.all()
    return render(request, 'echos/echo_detail.html', dict(echo=echo, waves=waves))


@login_required
def add_wave(request: HttpRequest, echo_pk: int) -> HttpResponse:
    echo = Echo.objects.get(pk=echo_pk)
    if request.method == 'POST':
        if (form := AddWaveForm(request.POST)).is_valid():
            wave = form.save(commit=False)
            wave.user = request.user
            wave.echo = echo
            wave.save()
            return redirect('echos:echo-detail', echo_pk=echo.pk)
    else:
        form = AddWaveForm()
    return render(request, 'echos/add_wave.html', dict(form=form))
