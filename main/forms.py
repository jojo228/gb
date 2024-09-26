from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from . import models



class SearchForm(forms.Form):
    prix_par_nuit = forms.IntegerField(required=False)
    prix_par_semaine = forms.IntegerField(required=False)
    prix_par_mois = forms.IntegerField(required=False)
    

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )