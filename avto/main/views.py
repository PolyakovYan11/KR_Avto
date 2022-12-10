from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AdForm, RegisterUserForm, LoginUserForm, UpdateUserForm
from .models import Ad, Profiles, Favorites
from django.views.generic import DetailView, UpdateView, DeleteView


def home(request):
    ad = Ad.objects.all()
    fav = Favorites.objects.all()
    return render(request, 'main/home.html', {'ad': ad, 'fav': fav})


def profile(request):
    mad = Ad.objects.all()
    return render(request, 'main/profile.html', {'mad': mad})


def favorite(request):
    fad = Favorites.objects.all()
    return render(request, 'main/favorite.html', {'fad': fad})


def settings(request):
    return render(request, 'main/settings.html')


def adplace(request, user_id):
    error = ''
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            a = Ad()
            a.mark = request.POST['mark']
            a.model = request.POST['model']
            a.age = request.POST['age']
            a.body = request.POST['body']
            a.shift = request.POST['shift']
            a.mileage = request.POST['mileage']
            a.engine = request.POST['engine']
            a.volume = request.POST['volume']
            a.driveunit = request.POST['driveunit']
            a.vin = request.POST['vin']
            a.city = request.POST['city']
            a.price = request.POST['price']
            a.comment = request.POST['comment']
            a.image = request.FILES['image']
            a.profile = Profiles.objects.get(pk=user_id)
            a.save()
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


def ad(request):
    return render(request, 'main/ad.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('sign')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/sign.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class AdDetailView(DetailView):
    model = Ad
    template_name = 'main/ad.html'
    context_object_name = 'advert'


def addfavorite(request, user_id, ad_id):
    for el in Favorites.objects.all():
        if (user_id == el.profile.id) & (ad_id == el.ad.id):
            return redirect('home')
    addf = get_object_or_404(Ad, pk=ad_id)
    prf = get_object_or_404(Profiles, pk=user_id)
    f = Favorites()
    f.ad = addf
    f.profile = prf
    f.save()
    return redirect('home')


class AdUpdateView(UpdateView):
    model = Ad
    template_name = 'main/adplace.html'

    form_class = AdForm


class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/profile'
    template_name = 'main/delete.html'


class ProfileUpdateView(UpdateView):
    model = Profiles
    template_name = 'main/changedata.html'
    success_url = '/settings'

    form_class = UpdateUserForm


class FavDeleteView(DeleteView):
    model = Favorites
    success_url = '/favorite'
    template_name = 'main/deletefav.html'

