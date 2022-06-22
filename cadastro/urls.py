from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cadastro_endereco.urls')),
    path('admin/', admin.site.urls),
]
