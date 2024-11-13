from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render

from .forms import EditWaveForm
from .models import Wave


@login_required
def edit_wave(request: HttpRequest, wave_pk: str) -> HttpResponse:
    wave = Wave.objects.get(pk=wave_pk)
    if wave.user != request.user:
        return HttpResponseForbidden('Error 403 - Forbidden')
    if request.method == 'POST':
        if (form := EditWaveForm(request.POST, instance=wave)).is_valid():
            wave = form.save(commit=False)
            wave.save()
            return redirect('echos:echo-detail', echo_pk=wave.echo.pk)
    else:
        form = EditWaveForm(instance=wave)
    return render(request, 'waves/edit_wave.html', dict(form=form, wave=wave))


@login_required
def delete_wave(request: HttpRequest, wave_pk: str) -> HttpResponse:
    wave = Wave.objects.get(pk=wave_pk)
    if wave.user != request.user:
        return HttpResponseForbidden('Error 403 - Forbidden')
    wave.delete()
    return render(request, 'waves/delete_wave.html', dict(wave=wave))
