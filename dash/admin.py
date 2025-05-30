# dash/admin.py
from django.contrib import admin
from .models import Operacao  # Importa especificamente o modelo Operacao


# Usar o decorador @admin.register é uma forma moderna
@admin.register(Operacao)
class OperacaoAdmin(admin.ModelAdmin):
    list_display = (
        'ativo',
        'lado',
        'quantidade',       # Campo atualizado
        'preco_operacao',   # Campo atualizado
        'data_operacao',    # Campo novo/atualizado
        'user_email',       # Método personalizado para mostrar o email
        'conta_selecionada',  # Campo novo
        'corretagem',       # Campo novo
        'tags',             # Campo novo
        'data_criacao_registro',  # Timestamp
    )
    list_filter = (
        'user',             # Filtra pelo objeto de usuário
        'lado',
        'ativo',
        'conta_selecionada',
        'data_operacao',
        'tags',             # Pode ser útil para filtrar por tags
    )
    search_fields = (
        'ativo',
        'user__email',      # Pesquisar pelo email do usuário
        'conta_selecionada',
        'tags',
        'anotacoes',        # Permitir busca nas anotações
    )
    # Usar a data da operação para navegação hierárquica
    date_hierarchy = 'data_operacao'

    # Método para exibir o email do usuário no list_display
    # Isso é útil porque 'user' por padrão mostraria o __str__ do CustomUser,
    # que já é o email, mas explicitar pode ser bom.
    def user_email(self, obj):
        if obj.user:
            return obj.user.email
        return None
    user_email.short_description = 'Usuário (Email)'  # Nome da coluna no admin

    # Para campos que você não quer que sejam editáveis diretamente na lista (opcional)
    # list_editable = ('tags', 'anotacoes')

    # Para organizar os campos no formulário de edição do admin (opcional, mas bom para formulários grandes)
    fieldsets = (
        (None, {
            'fields': ('user', 'conta_selecionada', 'ativo', 'lado')
        }),
        ('Detalhes da Operação', {
            'fields': ('quantidade', 'preco_operacao', 'data_operacao', 'horario_operacao', 'corretagem')
        }),
        ('Informações Adicionais', {
            'fields': ('anotacoes', 'tags')
        }),
        ('Campos de Outra Fonte (Não editáveis aqui)', {
            'classes': ('collapse',),  # Oculta por padrão
            'fields': ('total', 'total_executado'),
        }),
        ('Timestamps (Automáticos)', {
            'classes': ('collapse',),
            'fields': ('data_criacao_registro', 'data_atualizacao_registro'),
        }),
    )
    # Campos que são apenas para leitura no formulário de edição
    readonly_fields = ('data_criacao_registro',
                       'data_atualizacao_registro', 'total', 'total_executado')

# Se você não usar o decorador @admin.register(Operacao) acima,
# descomente a linha abaixo e remova o decorador:
# admin.site.register(Operacao, OperacaoAdmin)
