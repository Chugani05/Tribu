from django.contrib.auth.decorators import login_required
from .utils import check_owner
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
        if (form := AddEchoForm(request.user, request.POST)).is_valid():
            echo = form.save()
            return redirect('echos:echo-list')
    else:
        form = AddEchoForm(request.user)
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
@check_owner
def edit_echo(request: HttpRequest, echo_pk: int) -> HttpResponse|HttpResponseForbidden:
    echo = Echo.objects.get(pk=echo_pk)
    if request.method == 'POST':
        if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
            echo.id = echo_pk
            echo = form.save()
            return redirect('echos:echo-list')
    else:
        form = EditEchoForm(instance=echo)
    return render(request, 'echos/edit_echo.html', dict(form=form, echo=echo))


@login_required
@check_owner
def delete_echo(request: HttpRequest, echo_pk: int) -> HttpResponse|HttpResponseForbidden:
    echo = Echo.objects.get(pk=echo_pk)
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
            return redirect(echo)
    else:
        form = AddWaveForm()
    return render(request, 'echos/add_wave.html', dict(form=form))
