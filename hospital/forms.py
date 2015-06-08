from django import forms

from hospital.models import HospitalDirection, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
