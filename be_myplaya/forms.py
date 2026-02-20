import re

from django import forms
from .models import RequestCall,TransferRX

class RequestCallForm(forms.ModelForm):
    class Meta:
        model = RequestCall
        fields = '__all__'

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

class TransferRXForm(forms.ModelForm):
    class Meta:
        model = TransferRX
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "First Name",
                "style": "height:55px"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "Last Name",
                "style": "height:55px"
            }),
            "date_of_birth": forms.DateInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "type": "date",
                "style": "height:55px"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "Phone Number",
                "style": "height:55px"
            }),
            "address_line_1": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "Address Line 1",
                "style": "height:55px"
            }),
            "address_line_2": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "Address Line 2",
                "style": "height:55px"
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "City",
                "style": "height:55px"
            }),
            "state": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "State",
                "style": "height:55px"
            }),
            "zip_code": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "Zip Code",
                "style": "height:55px"
            }),
            "pharmacy_name": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "Pharmacy Name",
                "style": "height:55px"
            }),
            "pharmacy_phone_number": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "Pharmacy Phone Number",
                "style": "height:55px"
            }),
            "rx_number": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "Rx Number",
                "style": "height:55px",
                
            }),
            "medicine_first_letters": forms.TextInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "placeholder": "First 3 letters of medicine: XXX",
                "style": "height:55px",
                "maxlength": "3",
                "minlength": "3"
            }),
            "medicine_needed_date": forms.DateInput(attrs={
                "class": "form-control border-1 bg-light px-4",
                "type": "date",
                "style": "height:55px"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            css_class = self.fields[field].widget.attrs.get('class', '')
            self.fields[field].widget.attrs['class'] = css_class + ' form-control'

            if self.errors.get(field):
                self.fields[field].widget.attrs['class'] += ' is-invalid'

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", "").strip()

        if not first_name:
            raise forms.ValidationError("First name is required.")

        # Allow letters, spaces, hyphens, apostrophes
        if not re.match(r"^[A-Za-z\s'-]+$", first_name):
            raise forms.ValidationError(
                "First name can only contain letters, spaces, hyphens, and apostrophes."
            )

        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name", "").strip()

        if not last_name:
            raise forms.ValidationError("Last name is required.")

        if not re.match(r"^[A-Za-z\s'-]+$", last_name):
            raise forms.ValidationError(
                "Last name can only contain letters, spaces, hyphens, and apostrophes."
            )

        return last_name

    # ✅ Validations (your code – works fine)
    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"]
        return phone.as_national
    
    def clean_rx_number(self):
        rx = self.cleaned_data.get("rx_number")

        if len(rx) != 7:
            raise forms.ValidationError("RX number must be exactly 7 characters.")

        return rx

    def validate_us_phone(value):
        pattern = r"^\+1\d{10}$|^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
        if not re.match(pattern, value):
            raise forms.ValidationError("Enter a valid US phone number.")

        class TransferRXForm(forms.ModelForm):

            phone_number = forms.CharField(validators=["validate_us_phone"])
            pharmacy_phone_number = forms.CharField(validators=["validate_us_phone"])