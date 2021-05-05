from django import forms
from .models import *

class ArtworkImageForm(forms.ModelForm):

    class Meta:
        model = ArtworkImage
        fields = ['image']