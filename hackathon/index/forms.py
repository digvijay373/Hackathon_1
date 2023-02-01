from django.forms import ModelForm
from django import forms
from .models import Info

class UploadForm(ModelForm):
    class Meta:
        model = Info
        fields = ['GPA', 'SATM', 'SATE', 'ACT']