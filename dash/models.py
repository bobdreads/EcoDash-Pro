# dash/models.py
from django.db import models
from django.conf import settings


class Operacao(models.Model):
    LADO_CHOICES = [
        ('COMPRA', 'Compra'),
        ('VENDA', 'Venda'),
    ]

    # Relacionamento com o usuário
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # Alterado para evitar possível conflito com 'operacoes' do seu modelo original se ele for usado em outro app
        related_name='operacoes_usuario'
    )

    # Campos do Formulário
    conta_selecionada = models.CharField(
        "Conta Selecionada", max_length=100, blank=True, null=True)
    lado = models.CharField("Lado", max_length=6, choices=LADO_CHOICES)
    ativo = models.CharField("Ativo", max_length=100, blank=True, null=True)
    # Recebe a "Quantidade" do formulário
    quantidade = models.DecimalField(
        "Quantidade", max_digits=10, decimal_places=2, blank=True, null=True)
    data_operacao = models.DateField("Data da Operação", blank=True, null=True)
    horario_operacao = models.TimeField(
        "Horário da Operação", blank=True, null=True)
    preco_operacao = models.DecimalField(
        # Antigo preco_medio
        "Preço da Operação", max_digits=10, decimal_places=2, blank=True, null=True)
    corretagem = models.DecimalField(
        "Corretagem", max_digits=10, decimal_places=2, null=True, blank=True)
    anotacoes = models.TextField("Anotações", blank=True, null=True)
    # Tags separadas por vírgula
    tags = models.CharField("Tags", max_length=255, blank=True, null=True)

    corretora_info_adicional = models.CharField(
        "Corretora Info Adicional", max_length=255, blank=True, null=True)

    # Campos do seu modelo original que vêm de outro lugar (não preenchidos por este formulário)
    total = models.DecimalField(
        "Total (Outra Fonte)", max_digits=12, decimal_places=2, blank=True, null=True)
    total_executado = models.DecimalField(
        "Total Executado (Outra Fonte)", max_digits=12, decimal_places=2, blank=True, null=True)

    # Opcional: Se 'corretora' do seu modelo original tem um propósito diferente de 'conta_selecionada'

    # Timestamps automáticos para o registro
    data_criacao_registro = models.DateTimeField(
        "Data de Criação do Registro", auto_now_add=True)
    data_atualizacao_registro = models.DateTimeField(
        "Data de Atualização do Registro", auto_now=True)

    def __str__(self):
        lado_display = self.get_lado_display() if self.lado else "N/D"
        ativo_display = self.ativo if self.ativo else "N/D"
        # Certifique-se que self.user existe ou trate o None
        user_email = self.user.email if self.user else "N/D"
        return f"{lado_display} de {ativo_display} (Usuário: {user_email})"

    class Meta:
        verbose_name = "Operação de Trade"
        verbose_name_plural = "Operações de Trade"
        ordering = ['-data_operacao', '-horario_operacao']
