# dash/forms.py
from django import forms
from .models import Operacao


class OperacaoForm(forms.ModelForm):
    CONTA_CHOICES = [
        ('', 'Escolha uma conta'),  # Opção vazia como placeholder
        ('CONTA_XPTO_01', 'Conta Principal XPTO'),  # Use valores reais e rótulos
        ('CONTA_ABC_02', 'Conta Secundária ABC'),
        # Adicione mais contas conforme necessário
    ]

    # Definindo o campo explicitamente no formulário para adicionar choices
    conta_selecionada = forms.ChoiceField(
        choices=CONTA_CHOICES,
        label="Conta",  # Você pode definir o label aqui também
        widget=forms.Select(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5'
        })
    )

    LADO_FORM_CHOICES = [  # Definindo as choices EXATAS que queremos no form
        ('COMPRA', 'Compra'),
        ('VENDA', 'Venda'),
    ]

    lado = forms.ChoiceField(
        choices=LADO_FORM_CHOICES,
        widget=forms.RadioSelect(),  # Você pode adicionar attrs para classes aqui se quiser
        required=True,  # Explicitamente obrigatório
        label="Lado"  # Label customizado se desejar
    )

    class Meta:
        model = Operacao
        fields = [
            'conta_selecionada',  # Já está aqui e será usado o campo definido acima
            'lado',
            'ativo',
            'quantidade',
            'data_operacao',
            'horario_operacao',
            'preco_operacao',
            'corretagem',
            'anotacoes',
            'tags',
        ]
        widgets = {
            # Remova 'conta_selecionada' daqui, pois já definimos o campo e o widget acima
            'data_operacao': forms.DateInput(attrs={'type': 'date', 'id': 'id_data_operacao_field', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5'}),
            'horario_operacao': forms.TimeInput(attrs={'type': 'time', 'id': 'id_horario_operacao_field', 'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5'}),
            'lado': forms.RadioSelect(),
            'ativo': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5', 'placeholder': 'Ex: PETR4, WINDFUT'}),
            'quantidade': forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5', 'placeholder': 'Ex: 100'}),
            'preco_operacao': forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5', 'placeholder': 'Ex: 25,50'}),
            'corretagem': forms.NumberInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5', 'placeholder': 'Ex: 4,90'}),
            'anotacoes': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-cyan-600 focus:border-cyan-600', 'rows': 4, 'placeholder': 'Detalhes sobre a operação...'}),
            'tags': forms.HiddenInput(attrs={'id': 'id_tags_hidden_field_para_js'}),
        }
        labels = {  # Labels definidos aqui serão usados se não definidos no campo explícito
            'preco_operacao': 'Preço',
            'data_operacao': 'Data',
            'horario_operacao': 'Horário',
        }
