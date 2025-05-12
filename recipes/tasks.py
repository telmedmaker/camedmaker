from dashboard.models import MedicationRequestAnswer
from .utils import create_signed_pdf_recipes
from collections import defaultdict


def process_recipe_requests():
    requests = MedicationRequestAnswer.objects.filter(was_processed=False)
    requests_by_doctor = defaultdict(list)
    for req in requests:
        requests_by_doctor[req.doctor_id].append(req)

    for doctor_id, requests in requests_by_doctor.items():
        # if not request.was_approved:
        #     request.was_processed = True
        #     request.save()
        #     continue

        create_signed_pdf_recipes(requests)
        # request.was_processed = True
        # request.save()
