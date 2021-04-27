from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from home import urls as home_urls
from django.contrib.auth.views import LoginView as auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
