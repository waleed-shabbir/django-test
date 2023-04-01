from rest_framework import serializers
from .models import BoardingPass


class BoardingPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardingPass
        fields = '__all__'

    def create(self, validated_data):
        return BoardingPass(**validated_data)