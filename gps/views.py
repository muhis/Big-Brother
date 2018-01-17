from django.http import HttpResponse
from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from gps.models import Coordinate
# Create your views here.



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinate
        fields = ('longitude', 'latitude', 'create_time')


class CoordinateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordinateviewSet(viewsets.ModelViewSet):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer
    
    def get_queryset(self, **kwargs):
        return Coordinate.objects.filter(user=self.request.user)

