from django import forms
from .models import Car, Seller

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('make','model', 'img_url','trim', 'milage', 'color','name')

class SellerForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ('name', 'phone', 'address','web_site', 'logo')

# class ImageUploadForm(forms.Form):
#        image = ('img_url')
