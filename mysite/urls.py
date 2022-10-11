from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

app_name="myproject"
urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('g/', include('galleria.urls', namespace='galleria')),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)