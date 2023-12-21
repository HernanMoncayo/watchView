# De esta forma funcionan las vistas jajaja

#  from django.urls import path, re_path, include
# from apps.home import views
# from rest_framework import routers # Api

# router = routers.DefaultRouter()
# router.register(r'director-rest', views.DirectorViewSet)
# router.register(r'movie-rest', views.MovieViewSet)
# router.register(r'plataform-rest', views.PlataformViewSet)

# urlpatterns = [
#     path('', views.index, name='home'),

#     re_path(r'^.*\.*', views.pages, name='pages'),
#     path('api/', include('rest_framework.urls', namespace = 'rest_framework'))
# ]

# De esta forma funciona la api ----------------------------
from django.urls import path, include, re_path
from rest_framework import routers
from apps.home import views
from .views import index, pages, DirectorViewSet, MovieViewSet, PlataformViewSet

# n--
router = routers.DefaultRouter()
router.register(r'director-rest', DirectorViewSet)
router.register(r'movie-rest', MovieViewSet)
router.register(r'plataform-rest', PlataformViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include(router.urls)),  # Agregamos las URLs de la API--

    # La siguiente línea manejará todas las rutas no coincidentes con las anteriores.
    # Asegúrate de que esta línea esté al final.--
    path('<path:route>/', pages, name='pages'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]
