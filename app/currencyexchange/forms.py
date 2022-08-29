from django import forms



class CurrExch(forms.Form):

    amount = forms.IntegerField(label='Количество', widget=forms.NumberInput(attrs={"class": "form-control"}))
    from_curr = forms.ChoiceField(label='Исходная валюта', widget=forms.Select(attrs={"class": "form-control"}))
    to_curr = forms.ChoiceField(label='Желаемая валюта', widget=forms.Select(attrs={"class": "form-control"}))
