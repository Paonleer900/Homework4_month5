from rest_framework import serializers
from .models import Director, Movie, Review

# Сериализатор для Director
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Имя должно содержать не менее 3 символов.")
        return value

# Сериализатор для Movie
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Название фильма должно быть не короче 2 символов.")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Описание фильма не может быть пустым.")
        return value

# Сериализатор для Review
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Рейтинг должен быть в диапазоне от 1 до 5.")
        return value

    def validate_text(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Отзыв должен быть не короче 10 символов.")
        return value
