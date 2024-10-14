from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Имя режиссера должно содержать минимум 2 символа.")
        return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    # Валидация поля 'title' для модели Movie
    def validate_title(self, value):
        if len(value) < 1:
            raise serializers.ValidationError("Название фильма не может быть пустым.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    # Валидация поля 'stars' для модели Review (рейтинг должен быть от 1 до 5)
    def validate_stars(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Рейтинг должен быть от 1 до 5.")
        return value
