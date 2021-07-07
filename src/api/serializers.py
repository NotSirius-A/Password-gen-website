from rest_framework import serializers


class CustomSerializer(serializers.Serializer):
    """
    serializes python dict:
    'words': int,
    'symbols': bool,
    'quantity': int,
    'passwords': list, 
    """

    words = serializers.IntegerField()
    symbols = serializers.BooleanField()
    quantity = serializers.IntegerField()
    passwords = serializers.ListField()
