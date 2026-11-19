from django import forms
from .models import Morador, Funcionario, Entrega, Entrada, Ocorrencia

class EstiloBootstrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

class MoradorForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = Morador
        fields = ['nome', 'cpf', 'telefone', 'bloco', 'apartamento']

class FuncionarioForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cargo', 'turno', 'telefone']

class EntregaForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = Entrega
        fields = ['morador', 'descricao', 'retirado']

class EntradaForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['nome_visitante', 'documento', 'morador_destino']

class OcorrenciaForm(EstiloBootstrapMixin, forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['titulo', 'descricao', 'funcionario']