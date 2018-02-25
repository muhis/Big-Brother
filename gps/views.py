from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from gps.models import Coordinate
# Create your views here.


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ('latitude', 'longitude', 'create_time')


class CreateCoordinate(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        user = User.objects.get(pk=1)
        point = Coordinate(**request.data)
        point.user = user
        point.save()
        return Response(model_to_dict(point))
        

class CoordinateviewSet(generics.ListCreateAPIView):
    serializer_class = CoordinateSerializer
    permission_classes = []
    authentication_classes = []

    def get_queryset(self, **kwargs):
        """
        Get all coordinates for the requested user
        """
        user = self.request.user
        if isinstance(user, AnonymousUser):
            user = User.objects.get(pk=1)
        return Coordinate.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        if isinstance(user, AnonymousUser):
            user = User.objects.get(pk=1)
        serializer.validated_data['user'] = user
        return super(CoordinateviewSet, self).perform_create(serializer)


