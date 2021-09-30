from django import forms
import datetime

CHOICES = ['show int status', 'show run']

class CmdForm(forms.Form):

    command = forms.CharField(label='Command to execute', initial='show int status')
    # command = forms.ChoiceField(label='Command to execute', widget=forms.RadioSelect(), choices=CHOICES)
