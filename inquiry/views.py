import random
import string
import textwrap
from datetime import timedelta
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from accounts.serializers import UserSerializer
from common.utils import send_email
from inquiry.models import MedicationRequestOTP, Product
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
import json

from inquiry.serializers import DoctorSerializer, MedicationRequestSerializer

User = get_user_model()


class SendInquiryView(View):
    def get(self, request, uuid=None):
        context = {"products": Product.objects.all()}

        if uuid:
            otp = MedicationRequestOTP.objects.filter(id=uuid, expiration__gte=timezone.now()).first()
            if otp:
                context["user_id"] = otp.user.id

        return render(request, "inquiry/index.html", context)


class ProductsListView(View):
    def get(self, request):
        return JsonResponse(list(Product.objects.values_list("name", flat=True)), safe=False)


class DoctorsListView(View):
    def get(self, request):
        return JsonResponse(DoctorSerializer(User.objects.filter(role="doctor"), many=True).data, safe=False)


class UserView(APIView):
    def post(self, request):
        username = request.data.get("username")
        if not username:
            return JsonResponse(status=400, data={"username": ["This field is required."]})

        user = User.objects.filter(username=username).first()
        serializer = UserSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
            print("[ERROR]", serializer.errors)
            return JsonResponse(status=400, data=serializer.errors)

        new_user = serializer.save()

        # Don't allow interjection of ids of doctors
        if new_user.role != "patient":
            return JsonResponse(status=400, data={"user_id": ["This field must be a patient."]})

        # Create a new OTP entry, which can be used to create a new MedicationRequest, making
        # sure that the user is the owner of the email.
        otp = MedicationRequestOTP.objects.create(user=new_user, expiration=timezone.now() + timedelta(days=1))

        send_email(
            email=user.username,
            subject="Medicanova: Rezeptanfrage fortsetzen",
            text=f"""Sehr geehrte/r {user.full_name},

            Bitte klicken Sie auf folgenden Link um deine Rezeptanfrage fortzusetzen:

            http://localhost:8000/fragebogen/{otp.id}

            Beste Grüße,
            Ihr Medicanova-Team""",
        )

        return JsonResponse(status=200, data={})


class SubmitFormView(APIView):
    def post(self, request):
        data = request.data

        def _generate_number():
            def _random():
                return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))

            return f"{_random()}-{_random()}"

        data["number"] = _generate_number()

        user = User.objects.filter(id=data["user_id"]).first()
        if not user:
            return JsonResponse(status=400, data={"user_id": ["This field is required."]})

        # Don't allow interjection of ids of doctors
        if user.role != "patient":
            return JsonResponse(status=400, data={"user_id": ["This field must be a patient."]})

        serializer = MedicationRequestSerializer(data=data)
        if not serializer.is_valid():
            print("[ERROR]", serializer.errors)
            return JsonResponse(status=400, data=serializer.errors)

        medication_request = serializer.save()

        send_email(
            email=medication_request.user.username,
            subject="Bestätigung Ihrer Behandlungsanfrage",
            text=f"""Sehr geehrte/r {medication_request.user.full_name},

            vielen Dank für Ihre Anfrage. Ihr Anliegen wurde erfolgreich erfasst und wird nun von einem unserer Ärzte geprüft.

            Nach der ärztlichen Bewertung erhalten Sie alle relevanten Unterlagen, einschließlich einer Rechnung, eines Arztbriefs und – falls verordnet – eines Rezepts.

            Ihre Vorgangsnummer: {medication_request.number}

            Für weitere Fragen stehen wir Ihnen gerne zur Verfügung.

            Beste Grüße
            Ihr Medicanova-Team""",
        )

        return JsonResponse(status=200, data={"number": data["number"]})
