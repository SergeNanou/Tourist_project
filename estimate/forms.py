from django import forms

class EstimateForm(forms.Form):
    localite = forms.CharField(max_length=100)
    nombre_de_personnes  = forms.IntegerField()
    nbre_etoile_hotel  = forms.IntegerField()
    forme_de_tourisme = forms.CharField(max_length=100)
    emails = forms.EmailField()
    nombre_de_lieux_a_visiter  = forms.IntegerField()
    types_de_transport = forms.CharField(max_length=200)
    commentaires = forms.CharField(widget=forms.Textarea)