from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # pages = etusivu
    path('', include('pages.urls')),
    path('g/', include('galleria.urls')),
    path('admin/', admin.site.urls),
]
