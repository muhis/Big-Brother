from django.urls import path, include
from django.views.generic import TemplateView
from gps.views import CoordinateviewSet


urlpatterns = [
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
    )),
    path('', CoordinateviewSet.as_view(), name='gps_create_list'),
    path('track/', TemplateView.as_view(template_name="index.html"), name='track')
]
