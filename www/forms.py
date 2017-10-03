from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    title = forms.CharField(label='Cargo', max_length=100)
    image = forms.CharField(label='URL de imagen', max_length=200)
    mapa = forms.CharField(label='Ubicacion', max_length=200)