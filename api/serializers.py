from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=122)
    email = serializers.CharField(max_length=122)
    phone = serializers.CharField(max_length=12)
    desc = serializers.CharField(max_length=122)
    date = serializers.DateField