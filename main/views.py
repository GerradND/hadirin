from datetime import datetime
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Presensi
from .forms import IsiPresensi
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.views import generic
from .forms import UpdateProfile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.user.is_superuser:
        return redirect('role_divisi:role_divisi_list')
    else:
        return redirect('main:presensi')

@login_required
def profil(request):
    return render(request, 'main/profil.html')

@login_required
def profil_edit(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('main:profil'))
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'main/profilEdit.html', args)

## def presensi(request):
    ## return render(request, 'main/presensi.html')
@method_decorator(login_required, name='dispatch')
class presensi(generic.ListView):
    model =  Presensi
    template_name = 'main/presensi.html'
    def get_queryset(self):
        user = self.request.user
        queryset = Presensi.objects.all().filter(user=user)
        return (queryset)
        
@login_required
def presensi_edit(request):
    args = {}

    if request.method == 'POST':
        form = IsiPresensi(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('main:presensi'))
    else:
        form = IsiPresensi(initial={'masuk': datetime.now(), 'user': request.user})

    args['form'] = form
    return render(request, 'main/presensiEdit.html', args)
