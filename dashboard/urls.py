from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/change_password/', views.change_password, name='change_password'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('outlet/', include('outlet.urls')),
    path('', views.home, name='home')
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
