from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import AddEchoForm
from .models import Echo


def echo_list(request: HttpRequest) -> HttpResponse:
    echos = Echo.objects.all()
    return render(request, 'echos/echo-list.html', dict(echo=echos))


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
    return render(request, 'echos:add-echo', dict(form=form))


def echo_detail(request: HttpRequest, echo_id: str) -> HttpResponse:
    echo = Echo.objects.get(id=echo_id)
    return render(request, 'echos/echo-detail.html', dict(echo=echo))


def edit_echo(request, echo_id):
    task = Echo.objects.get(id=echo_id)
    if request.method == 'POST':
        if (form := AddEchoForm(request.POST, instance=echo)).is_valid():
            echo = form.save(commit=False)
            echo.id = echo_id
            echo.save()
            return redirect('echos:echo-list')
    else:
        form = AddEchoForm(instance=task)
    return render(request, 'echos/edit-echo.html', dict(form=form, echo=echo))


def delete_echo(request, echo_id):
    echo = Echo.objects.get(id=echo_id)
    echo.delete()
    return render(request, 'echos/delete-echo.html', dict(echo=echo))


def echo_waves(request: HttpRequest) -> HttpResponse:
    pass
