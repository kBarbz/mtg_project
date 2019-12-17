from django import forms

class DiceForm(forms.Form):
    rolls = forms.IntegerField(
    min_value=1,
    widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "rolls"
        })
    )
    size = forms.IntegerField(
        min_value=2,
        widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "size"
            }
        )
    )

class CoinForm(forms.Form):
    flips = forms.IntegerField(
    min_value=1,
    widget=forms.TextInput(attrs={
    "class": "form-control",
    "id": "flips"
        })
    )
    thumb = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-control",
            "id": "thumb"
            }
        )
    )
