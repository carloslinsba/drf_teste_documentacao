from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from carlosflix.views import ProgramaViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('programas', ProgramaViewSet, basename='programas')

schema_view = get_schema_view(
   openapi.Info(
      title="CarlosFlix",
      default_version='v1',
      description=" A system that enables controling films and series. ",
      terms_of_service="#",
      contact=openapi.Contact(email="carloslinsba [at] gmail [dot] com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
