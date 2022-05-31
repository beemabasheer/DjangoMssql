from datetime import date, timedelta
import datetime

from django import forms
from django.forms import BaseFormSet, BaseModelFormSet, formset_factory
from django.forms.models import modelformset_factory

from SalesTeam.models import SalesTeam

TYPE_CHOICES = (
    ("Search Engine", "Search Engine"),
    ("LinkedIn", "LinkedIn"),
    ("Social Media", "Social Media"),
    ("Through a friend", "Through a friend"),
    ("Others", "Others"),

)


class SalesTeamForm(forms.ModelForm):
    """
    Sales Team Form
    """
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(
        required=True)
    company = forms.CharField(required=True)
    hear_about_us = forms.ChoiceField(choices=TYPE_CHOICES, required=False)
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 5, 'rows': 8}), required=False)


    class Meta:
        model = SalesTeam
        fields = '__all__'

    def save(uid, product, self, commit=True):
        # save the response object
        response = super(ReviewForm, self).save(commit=False)
        #print(self.cleaned_data['review_text'])
        #response.survey = self.survey
        #user = uid
        tag = self.cleaned_data['tag']
        product = product
        review_text = self.cleaned_data['review_text']
        #created
        #updated 


        response.save()

        return response