from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from authentication.models import CustomUser


class Operacao(models.Model):  # Substitua 'Operacao' pelo nome que escolher
    # Campo para ligar ao CustomUser
    # Aqui assumimos que o CustomUser é o padrão do Django ou está em settings.AUTH_USER_MODEL
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='operacoes')

    # Campos baseados nas colunas do CSV
    corretora = models.CharField(
        "Corretora", max_length=255, blank=True, null=True)
    ativo = models.CharField("Ativo", max_length=100, blank=True, null=True)
    lado = models.CharField("Lado", max_length=50,
                            blank=True, null=True)  # Ex: Compra, Venda
    # Precisaremos saber o formato da data no CSV
    ultima_atualizacao = models.DateTimeField(
        "Última Atualização", blank=True, null=True)
    # Ou IntegerField se for sempre inteiro
    qtd = models.DecimalField(
        "Quantidade", max_digits=10, decimal_places=2, blank=True, null=True)
    preco_medio = models.DecimalField(
        "Preço Médio", max_digits=10, decimal_places=2, blank=True, null=True)
    qtd_executada = models.DecimalField(
        "Qtd. Executada", max_digits=10, decimal_places=2, blank=True, null=True)  # Ou IntegerField
    total = models.DecimalField(
        "Total", max_digits=12, decimal_places=2, blank=True, null=True)
    total_executado = models.DecimalField(
        "Total Executado", max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Ativo: {self.ativo} (Usuário: {self.user.username})"
