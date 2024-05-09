from django import forms


class ChatLinksForm(forms.Form):
    variant_id = forms.IntegerField()
    size_id = forms.IntegerField()
