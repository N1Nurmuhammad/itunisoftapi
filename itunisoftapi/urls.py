from decouple import config
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="ITUNISOFT",
        default_version='v1',
        description="API Docs",
        terms_of_service="",
        contact=openapi.Contact(url="https://t.me/N1Nurmuhammad", name="Developer Telegram", ),
        license=openapi.License(name="BSD License"),
    ),
    url=config('PRODUCTION_HOST'),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
