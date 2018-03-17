from django import forms

from .models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "address_street",
            'postal_code',
            'city',
            'country'
        )
