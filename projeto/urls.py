from django import urls
from projeto import core
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('projeto.core.urls')),
    path('produto/', include('projeto.produto.urls')),
    path('admin/', admin.site.urls),
]
