from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Medusa Light",
        default_version='v1',
        description="новостной сервис",
        contact=openapi.Contact(url="https://Medusa.Light"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('news/', include('src.tiding.api.urls')),
]
