from django import forms

class ChosePath(forms.Form):
    named_form_value = forms.CharField(label='Your Path', max_length=1)