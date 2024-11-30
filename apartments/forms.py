from django import forms
from apartments.models import Apartment

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField()
    email = forms.CharField(widget=forms.EmailInput)
    description = forms.CharField(widget=forms.Textarea)

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        # fields = '__all__'
        exclude = ('id', 'owner')
        # fields = ('id', 'name', 'longitude', 'likes')