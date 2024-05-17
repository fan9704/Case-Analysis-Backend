from rest_framework import serializers
from api.models import Case, Patient


class CaseGeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = "__all__"
        read_only_fields = ["id"]

        def create(self, validated_data):
            return Case.objects.create(
                user=Patient.objects.get(pk=validated_data["user"]).pk,
                background=validated_data["background"],
                clinical_findings=validated_data[" clinical_findings"],
                diagnostic_process=validated_data[" diagnostic_process"],
                intervention_and_treatment=validated_data["intervention_and_treatment"],
                outcome=validated_data["outcome"],
                discuss=validated_data["discuss"],
                pathology=validated_data["pathology"],
            )
