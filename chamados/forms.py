from django import forms
from .models import Chamado, Comentario 


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ["titulo", "descricao", "categoria", "prioridade"]
        
class GerenciarChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ["status", "agente"]        
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]