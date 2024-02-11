from django.forms import ModelForm, Textarea
from .models import *
from django import forms
from django.core.exceptions import ValidationError


# general function to style forms to inheret from here instead of default forms
class StylishForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})



class ReagentForm(StylishForm):
    class Meta:
        model = Reagent
        fields = ["reagent_name", "catalogue_no", "catalogue_url", "reagent_storage"]
        widgets = {
            "owner": forms.HiddenInput(),
        }
      