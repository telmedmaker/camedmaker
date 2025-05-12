from .models import MedicationRequest
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class MedicationRequestSerializer(serializers.ModelSerializer):
    # require the id to be provided
    user_id = serializers.UUIDField(required=True)

    class Meta:
        model = MedicationRequest
        fields = [
            "user_id",
            "number",
            "symptoms",
            "symptom_text",
            "symptom_severity",
            "symptom_duration",
            "was_already_treated",
            "previously_taken_medication",
            "previous_medication_details",
            "previously_taken_cannabis",
            "previous_cannabis_details",
            "doctor_wish",
            "medication_wish",
            "agreed_no_exclusion_criteria",
        ]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "full_name", "email"]
