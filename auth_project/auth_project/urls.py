from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Vistas de autenticación por defecto
    path('accounts/', include('accounts.urls')),             # Tus vistas personalizadas
]
