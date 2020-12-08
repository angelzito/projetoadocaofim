from django import forms
from .models import Cadastro


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['denuncia', 'hora', 'local', 'gravidade_alta_ou_muito_alta', 'porte', 'espécie', 'cor', 'contato_do_denunciante', 'teste', 'teste_dois']

