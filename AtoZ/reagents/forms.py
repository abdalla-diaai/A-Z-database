from django.forms import ModelForm, Textarea
from .models import *
from django import forms
from django.core.exceptions import ValidationError


# general function to style forms to inheret from here instead of default forms
class StylishForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control form-control-sm" "form-outline w-50"})

class ExperimentForm(StylishForm):
    class Meta:
        model = Experiment
        fields = ["title", "objective", "methods", "results", "summary", "upload"]
        widgets = {
            "owner": forms.HiddenInput(),
        }

class ReagentForm(StylishForm):
    class Meta:
        model = Reagent
        fields = ["reagent_name", "catalogue_no", "reagent_url", "reagent_supplier", "reagent_storage"]
        widgets = {
            "owner": forms.HiddenInput(),
        }
      
# form to upload a protocol
class UploadFile(StylishForm):
    upload = forms.FileField(required=False)
    class Meta:
        model = Protocol
        fields = [
            "title",
            "upload"
        ]
        widgets = {
            "owner": forms.HiddenInput(),
        }


class CellsForm(StylishForm):
    class Meta:
        model = CellLine
        fields = ["cell_name", "media", "genotype", "storage_position"]
        widgets = {
            "owner": forms.HiddenInput(),
        }
      

# form for reagents search
class ReagentSearch(forms.Form):
    search = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search Database", "class": "form-control"}
        ),
    )
    database_to_search = models.CharField(max_length=30)

# form for cells search
class CellsSearch(forms.Form):
    search = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search Database", "class": "form-control"}
        ),
    )
    database_to_search = models.CharField(max_length=30)

# form for protocols search
class ProtocolsSearch(forms.Form):
    search = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search Database", "class": "form-control"}
        ),
    )
    database_to_search = models.CharField(max_length=30)


