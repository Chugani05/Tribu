from django.contrib.auth.decorators import login_required
from .utils import check_owner
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import EditWaveForm
from .models import Wave


@login_required
@check_owner
def edit_wave(request: HttpRequest, wave_pk: str) -> HttpResponse:
    wave = Wave.objects.get(pk=wave_pk)
    if request.method == 'POST':
        if (form := EditWaveForm(request.POST, instance=wave)).is_valid():
            wave = form.save(commit=False)
            wave.save()
            return redirect('echos:echo-detail', echo_pk=wave.echo.pk)
    else:
        form = EditWaveForm(instance=wave)
    return render(request, 'waves/edit_wave.html', dict(form=form, wave=wave))


@login_required
@check_owner
def delete_wave(request: HttpRequest, wave_pk: str) -> HttpResponse:
    wave = Wave.objects.get(pk=wave_pk)
    wave.delete()
    return render(request, 'waves/delete_wave.html', dict(wave=wave))
