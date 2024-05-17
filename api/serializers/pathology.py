from rest_framework.serializers import ModelSerializer
from api.models import Pathology


class PathologyGeneralSerializer(ModelSerializer):
    class Meta:
        model = Pathology
        fields = "__all__"
        read_only_fields = ["id"]
