from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views
from .views import RegisterUser, LoginUser
from django.contrib import admin

urlpatterns = [
                  path('', views.home, name='home'),
                  path('profile', views.profile, name='profile'),
                  path('favorite', views.favorite, name='favorite'),
                  path('settings', views.settings, name='settings'),
                  path('adplace/<int:user_id>', views.adplace, name='adplace'),
                  path('<int:pk>/changedata', views.ProfileUpdateView.as_view(), name='changedata'),
                  path('reg', RegisterUser.as_view(), name='registration'),
                  path('sign', LoginUser.as_view(), name='sign'),
                  path('logout', views.logout_user, name='logout'),
                  path('<int:pk>', views.AdDetailView.as_view(), name='ad'),
                  path('addfavorite/<int:user_id>/<int:ad_id>', views.addfavorite, name='addfavorite'),
                  path('<int:pk>/update', views.AdUpdateView.as_view(), name='update'),
                  path('<int:pk>/delete', views.AdDeleteView.as_view(), name='delete'),
                  path('<int:pk>/deletefav', views.FavDeleteView.as_view(), name='deletefav'),
                  path("chat/", include("chat.urls")),
                  path("admin/", admin.site.urls),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
