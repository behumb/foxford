from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view as get_swagger_view
from drf_yasg import openapi

schema_view = get_swagger_view(
    openapi.Info(
        title='Foxford API',
        default_version='1.0.0',
        description='API documentation'
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('webinar.urls')),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]
