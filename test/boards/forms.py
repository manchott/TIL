import imp
from django import forms
from django import forms
from .models import Board


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title',)