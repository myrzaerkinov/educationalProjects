from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = "__all__"