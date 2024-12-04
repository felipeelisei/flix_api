from django.db.models import Avg
from rest_framework import serializers
from genres.serializers import GenreSerializer
from movies.models import Movie
from actors.serializers import ActorSerializer


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_realease_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('Nao pode ser menor que 1980')
        return value
    
    
class MovieListDetailSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'realease_date', 'rate', 'resume']
        
    def get_rate(self, obj):
        # agrega um campo a mais na query e calcula a media diretamente no ORM
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
    