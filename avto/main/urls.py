from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('favorite', views.favorite, name='favorite'),
    path('settings', views.settings, name='settings'),
    path('adplace', views.adplace, name='adplace'),
    path('changedata', views.changedata, name='changedata'),
    path('reg', views.reg, name='reg'),
    path('sign', views.sign, name='sign'),
    path('ad', views.ad, name='ad')
]