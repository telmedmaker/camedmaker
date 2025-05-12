from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "role",
            "full_name",
            "email",
            "birth_date",
            "address",
            "zip_code",
            "city",
            "phone",
            "checkbox_withdrawal",
            "checkbox_communication",
            "checkbox_data_sharing",
            "checkbox_data_policy",
            "checkbox_newsletter",
        ]
