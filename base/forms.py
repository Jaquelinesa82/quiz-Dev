from django.forms import ModelForm

from base.models import Aluno


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email']
