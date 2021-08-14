from rest_framework import serializers
from .models import IMDB


class IMDBSerializer(serializers.ModelSerializer):
    genre = serializers.JSONField()

    class Meta:
        model = IMDB
        fields = '__all__'

    def create(self, validated_data):
        return IMDB.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.popularity = validated_data.get('popularity', instance.popularity)
        instance.director = validated_data.get('director', instance.director)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
        instance.save()
        return instance

    def validate_genre(self, value):
        if type(value) != list:
            raise serializers.ValidationError("Genre must be a list")
        else:
            return value
