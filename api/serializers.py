from rest_framework import serializers

from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    _id = serializers.CharField(source="pk", read_only=True)
    favorite_food = serializers.CharField(
        source="favorite_food",
        max_length=100
        
    )

    favorite_emoji = serializers.CharField(
        source="favorite_emoji",
        max_length=20
        
    )

class Meta:
    model = Student
    fields = ["_id", "name", "favoriteFood", "favoriteEmoji"]