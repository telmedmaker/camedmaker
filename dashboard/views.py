from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from two_factor.views import OTPRequiredMixin
from common.mixins import DoctorLoginRequiredMixin
from dashboard.forms import MedicationRequestAnswerForm
from inquiry.models import MedicationRequest


class EvaluateMedicationRequestView(OTPRequiredMixin, DoctorLoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, number=None):
        open_requests = MedicationRequest.objects.filter(doctor_wish=self.request.user)

        if not open_requests.exists():
            return render(request, "dashboard/medication_requests_empty.html")

        if number:
            return render(
                request,
                "dashboard/medication_requests.html",
                {
                    "open_requests_count": len(open_requests),
                    "med_request": get_object_or_404(MedicationRequest, doctor_wish=self.request.user, number=number),
                },
            )

        return redirect("dashboard:evaluate-medication-request", number=open_requests[0].number)

    def post(self, request, number):
        form = MedicationRequestAnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard:evaluate-medication-request")
        else:
            return redirect("dashboard:evaluate-medication-request")
