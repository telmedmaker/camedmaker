from django import forms
from .models import MedicationRequestAnswer


class MedicationRequestAnswerForm(forms.ModelForm):

    # make private notes an optional field
    def __init__(self, *args, **kwargs):
        super(MedicationRequestAnswerForm, self).__init__(*args, **kwargs)
        self.fields["private_notes"].required = False

    class Meta:
        model = MedicationRequestAnswer
        fields = ["doctor", "medication_request", "diagnosis", "private_notes", "medication", "was_approved"]
