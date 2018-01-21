from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers, generics
from django.contrib.auth.models import User
from gps.models import Coordinate
# Create your views here.


class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ('latitude', 'longitude', 'create_time')


class CoordinateviewSet(generics.ListCreateAPIView):
    serializer_class = CoordinateSerializer
    permission_classes = []
    
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


