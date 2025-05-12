import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model

from common.models import TimeStampedModel


User = get_user_model()


class Product(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("created",)


class MedicationRequestOTP(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_requests_otp", null=True, blank=True
    )
    expiration = models.DateTimeField()


class MedicationRequest(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medication_requests", null=True, blank=True)
    number = models.CharField(max_length=12, primary_key=True)

    symptoms = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    symptom_text = models.TextField(blank=True, null=True)
    symptom_severity = models.IntegerField(blank=True, null=True)
    symptom_duration = models.CharField(max_length=200)
    was_already_treated = models.BooleanField()
    previously_taken_medication = models.BooleanField()
    previous_medication_details = models.TextField(null=True, blank=True)
    previously_taken_cannabis = models.BooleanField()
    previous_cannabis_details = models.TextField(null=True, blank=True)
    doctor_wish = models.ForeignKey(User, on_delete=models.CASCADE)
    medication_wish = models.JSONField()

    agreed_no_exclusion_criteria = models.BooleanField()

    class Meta:
        ordering = ("created",)
