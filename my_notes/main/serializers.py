from dataclasses import field
from rest_framework import serializers
from main.models import Note, Category


class NoteForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title')

class NoteForCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'description', 'category')

class CategoryForListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
