import fillpdf
from fillpdf import fillpdfs


input_pdf = "dashboard/static/dashboard/img/recipe-template.pdf"

data = {"medication": "Test"}

fillpdfs.write_fillable_pdf(input_pdf, "new.pdf", data, flatten=True)
