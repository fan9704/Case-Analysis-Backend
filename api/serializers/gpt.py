from rest_framework import serializers


class GPTRequestSerializer(serializers.Serializer):
    msg = serializers.CharField()
