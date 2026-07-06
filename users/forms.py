from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    widget=forms.PasswordInput(attrs={ "class=":"form-control", "placeholder":"Password"})

    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    widget=forms.PasswordInput(attrs={ "class=":"form-control", "placeholder":"Confirm Password"})

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}),
            "last_name": forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}),
            "username": forms.TextInput(attrs={"class":"form-control", "placeholder":"User Name"}),
            "email": forms.TextInput(attrs={"class":"form-control", "placeholder":"Email"}),
        }

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError(
                "password do not match."
            )
        return cleaned_data