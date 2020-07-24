from django import forms
from .models import Matzip

class MatForm(forms.ModelForm):
    class Meta:
        model = Matzip
        fields = ['title','body','image','image2']