from rest_framework import serializers


class CustomSerializer(serializers.Serializer):
    words = serializers.IntegerField()
    symbols = serializers.BooleanField()
    quantity = serializers.IntegerField()
    passwords = serializers.ListField()
