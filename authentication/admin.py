from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Campos visíveis na lista de usuários
    list_display = ('email', 'first_name', 'last_name',
                    'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    # Campos exibidos no formulário de edição do usuário no admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_staff',
         'is_active', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(RegistrationKey)
class RegistrationKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'is_used')
    list_filter = ('is_used',)
    search_fields = ('key',)


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    # Exibe o nome da carteira e o usuário no admin
    list_display = ('user', 'carteira')


@admin.register(Setup_user)
class Setup_userAdmin(admin.ModelAdmin):
    list_display = ('user', 'setup')


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = ('setup', 'description')


@admin.register(Taxas_user)
class Taxas_userAdmin(admin.ModelAdmin):
    list_display = [
        'taxas_id',
        'user',
        'taxas_acoes_brasileiras',
        'taxas_indice_futuro',
        'taxas_dolar_futuro',
        'corretagem_acoes_brasileiras',
        'corretagem_indice_futuro',
        'corretagem_dolar_futuro',
    ]
    search_fields = ['user', 'taxas_id']
