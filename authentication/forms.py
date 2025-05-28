from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser
from .models import CustomUser, RegistrationKey
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-2 focus:ring-fuchsia-50 focus:border-fuchsia-300 block w-full p-2.5",
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "••••••••",
                "class": "border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-2 focus:ring-fuchsia-50 focus:border-fuchsia-300 block w-full p-2.5",
            }
        ))
    remember_me = forms.BooleanField(
        required=False,  # O campo não é obrigatório
        initial=False,   # Valor padrão como False
        widget=forms.CheckboxInput(
            attrs={
                "class": "w-5 h-5 rounded border-gray-300 focus:outline-none focus:ring-0 checked:bg-dark-900"
            }
        ))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "João",
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "da Silva",
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "••••••••",
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "••••••••",
            }
        ))
    key = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Insira sua chave",
                "class": "border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-2 focus:ring-fuchsia-50 focus:border-fuchsia-300 block w-full p-2.5",
            }
        ),
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Classes para os inputs
        input_classes = "border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-2 focus:ring-fuchsia-50 focus:border-fuchsia-300 block w-full p-2.5"

        for field_name, field in self.fields.items():
            # Atualiza os widgets com classes personalizadas
            field.widget.attrs.update({'class': input_classes})

    def clean_key(self):
        key = self.cleaned_data.get('key')
        try:
            reg_key = RegistrationKey.objects.get(key=key, is_used=False)
        except RegistrationKey.DoesNotExist:
            raise forms.ValidationError("Chave inválida ou já utilizada.")
        return key
