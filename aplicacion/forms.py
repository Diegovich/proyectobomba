from django import forms

from aplicacion.models import CargaBomba, CargaCamioneta

class formularioCargaCamioneta(forms.ModelForm):
    class Meta:
        model = CargaCamioneta
        fields = '__all__'
        widgets = {
            'chofer':forms.TextInput(attrs={'class':'form-control'}),
            'bomba': forms.Select(attrs={'class':'form-select'}),
            'litrosCargados': forms.NumberInput(attrs={'class':'form-control'}),
            'kilometrajeActual':forms.NumberInput(attrs={'class':'form-control'})
        }
        labels = {
            'litrosCargados':'Litros Cargados',
            'kilometrajeActual':'Kilometraje Actual'
        }

class formularioCargaBomba(forms.ModelForm):
    class Meta:
        model = CargaBomba
        fields = '__all__'
        widgets = {
            'bomba' : forms.Select(attrs={'class':'form-select'}),
            'bombero' : forms.Select(attrs={'class':'form-select'}),
            'litrosCargados' : forms.NumberInput(attrs={'class':'form-control'})
        }
        labels = {
            'litrosCargados' : 'Litros Cargados'
        }