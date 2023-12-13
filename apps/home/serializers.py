from rest_framework import serializers
from apps.home.models import Director, Movie, Plataform

class DirectorSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ('__all__')

class MovieSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

class PlataformSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plataform
        fields = ('__all__')