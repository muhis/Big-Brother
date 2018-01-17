from django.urls import path, include
from rest_framework import routers
from gps.views import UserViewSet, CoordinateviewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'history', CoordinateviewSet)

urlpatterns = [
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
    )),
    path('', include(router.urls)),
]
