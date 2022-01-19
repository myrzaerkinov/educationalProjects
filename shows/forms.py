from django import forms
from . import models

class ShowForm(forms.ModelForm):
    class Meta:
        model = models.TVShow
        fields = "__all__"
        # fields = (
        #     'title',
        #     'description',
        #     'image',
        #     'quantity',
        #     'genre',
        # )