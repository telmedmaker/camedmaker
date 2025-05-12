from django.db import models
from django.contrib.auth import get_user_model
from common.models import TimeStampedModel
from inquiry.models import MedicationRequest

User = get_user_model()


class MedicationRequestAnswer(TimeStampedModel):
    medication_request = models.OneToOneField(MedicationRequest, on_delete=models.CASCADE, related_name="answer")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medication_request_answers")

    diagnosis = models.TextField(null=True)
    private_notes = models.TextField(null=True)
    medication = models.TextField(null=True)

    was_approved = models.BooleanField(null=True)
    was_processed = models.BooleanField(default=False)
