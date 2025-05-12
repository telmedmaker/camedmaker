import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class RoleChoices(models.TextChoices):
    DOCTOR = "doctor", "Doctor"
    PATIENT = "patient", "Patient"


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=10, choices=RoleChoices.choices)

    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    checkbox_withdrawal = models.BooleanField(null=True)
    checkbox_communication = models.BooleanField(null=True)
    checkbox_data_sharing = models.BooleanField(null=True)
    checkbox_data_policy = models.BooleanField(null=True)
    checkbox_newsletter = models.BooleanField(default=False)

    @property
    def age(self):
        today = timezone.now().date()
        age = int(
            today.year
            - (self.birth_date.year)
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return age
