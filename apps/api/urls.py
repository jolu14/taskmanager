from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views.task_view import TaskViewSet
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)


SWAGGER_INFO = openapi.Info(
    title="API Documentation",
    default_version='v1',
    description="API Documentation for Task Mananger",
    terms_of_service="https://www.example.com/terms/",
    contact=openapi.Contact(email="contact@example.com"),
    license=openapi.License(name="BSD License"),
)

schema_view = get_schema_view(
   SWAGGER_INFO,
   public=True,
)


urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]