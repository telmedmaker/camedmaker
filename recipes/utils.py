from fillpdf import fillpdfs
from dashboard.models import MedicationRequestAnswer

from recipes.services.certifaction import CertifactionAPI


def create_blank_pdf(med_request_answer: MedicationRequestAnswer):
    input_pdf = "dashboard/static/dashboard/img/recipe-template.pdf"
    data = {"medication": "Test"}
    path = f"recipe-{med_request_answer.id}.pdf"
    fillpdfs.write_fillable_pdf(input_pdf, path, data, flatten=True)
    return path


def create_signed_pdf_recipes(med_request_answers: list[MedicationRequestAnswer]):
    pdf_paths = []
    for answer in med_request_answers:
        pdf_paths.append(create_blank_pdf(answer))

    certifaction = CertifactionAPI()

    objs = [
        {
            "pdf_path": pdf_path,
            "name": f"Rezept-{answer.medication_request.user.full_name.replace(' ', '-')}.pdf",
        }
        for answer, pdf_path in zip(med_request_answers, pdf_paths)
    ]
    request_url = certifaction.send_signing_request(objs, "gabri.marcan@gmail.com")
    print(request_url)


def qes_sign_recipe():
    pass
