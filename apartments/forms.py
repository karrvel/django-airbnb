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
        fields = '__all__'
        exclude = ('image', )
        # fields = ('id', 'name', 'longitude', 'likes')


    # custom field validation
    def clean_daily_price(self):
        daily_price = self.cleaned_data['daily_price']

        if daily_price == 0 or daily_price > 1000:
            raise forms.ValidationError("Daily price can not be zero or greater than $1000")
        
        return daily_price


    