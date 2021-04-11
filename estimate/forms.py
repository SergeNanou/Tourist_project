from django import forms

class EstimateForm(forms.Form):
    Localité = forms.CharField(max_length=100)
    Nombre_de_personnes  = forms.IntegerField()
    Type_d_hotel  = forms.IntegerField()
    Forme_de_tourisme = forms.CharField(max_length=100)
    Emails = forms.EmailField()
    Nombre_de_lieux_a_visiter  = forms.IntegerField()
    Types_de_transport = forms.CharField(max_length=100)
    Commentaires = forms.CharField(widget=forms.Textarea)