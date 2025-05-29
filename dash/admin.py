from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import *

# Classe de Admin para Operacao (NOVO)


class OperacaoAdmin(admin.ModelAdmin):
    list_display = (
        'ativo',
        'lado',
        'qtd',
        'preco_medio',
        'total_executado',
        'user',  # Mostra o __str__ do CustomUser
        'ultima_atualizacao',
    )
    list_filter = (
        'user',  # Filtra por utilizador
        'lado',   # Filtra por Compra/Venda
        'ativo',
        'corretora',
        'ultima_atualizacao'
    )
    search_fields = (
        'ativo',
        'user__username',  # Permite pesquisar pelo username do utilizador associado
        'corretora',
        'conta',
    )
    # Adiciona uma navegação hierárquica por data
    date_hierarchy = 'ultima_atualizacao'
    # Campos que não podem ser editados na admin


admin.site.register(Operacao, OperacaoAdmin)
