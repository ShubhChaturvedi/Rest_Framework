from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['id']
        # fields = ['name', 'roll', 'city']

    def validate(self, data):
        if (data['roll'] > 75 or data['roll'] <= 0):
            raise serializers.ValidationError({
                'error': 'Roll Number is not valid'
            })
        if data['name']:
            for i in data['name']:
                if i.isdigit():
                    raise serializers.ValidationError({
                        'error': 'Name should not be numeric'
                    })
        return data

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1