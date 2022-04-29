from dataclasses import field
from rest_framework import serializers
from main.models import Note, Category


class NoteForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title')

class NoteFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'description', 'category', 'is_done')
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class CategoryForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
