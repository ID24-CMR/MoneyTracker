from django import forms


from .models import Category

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category

        fields = [
            "name",
            "category_type",
            "color",
            "icon",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "category Name",
            }),

            "category_type": forms.Select(attrs={
                "class": "form-control",
            }),

            "color": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "icon": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "FontAwesome icon",
            }),
        }