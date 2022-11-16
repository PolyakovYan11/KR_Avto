from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AdForm
from .models import Ad


def home(request):
    ad = Ad.objects.all()
    return render(request, 'main/home.html', {'ad': ad})


def profile(request):
    return render(request, 'main/profile.html')


def favorite(request):
    return render(request, 'main/favorite.html')


def settings(request):
    return render(request, 'main/settings.html')


def adplace(request):
    error = ''
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = AdForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/adplace.html', data)


def changedata(request):
    return render(request, 'main/changedata.html')


def reg(request):
    return render(request, 'main/reg.html')


def sign(request):
    return render(request, 'main/sign.html')


def ad(request):
    return render(request, 'main/ad.html')
