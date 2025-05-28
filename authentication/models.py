from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Define email como identificador
    # Remove username como obrigatório
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class RegistrationKey(models.Model):
    key = models.CharField(max_length=50, unique=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return self.key


class Wallet(models.Model):
    # Define o nome do campo ID como wallet_id
    wallet_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='wallets')
    carteira = models.CharField(max_length=100)  # Nome da carteira

    def __str__(self):
        return f"{self.user.email} - {self.carteira}"


class Setup_user(models.Model):
    setup_user_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='setups')
    setup = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.email} - {self.setup}"


class Setup(models.Model):
    setup_id = models.AutoField(primary_key=True)
    setup = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return f"{self.setup} - {self.description}"


class Taxas_user(models.Model):
    # Chave primária auto-incremental
    taxas_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='taxas', default='1')
    taxas_acoes_brasileiras = models.DecimalField(
        max_digits=10, decimal_places=6)
    taxas_indice_futuro = models.DecimalField(
        max_digits=10, decimal_places=2)
    taxas_dolar_futuro = models.DecimalField(
        max_digits=10, decimal_places=2)
    corretagem_acoes_brasileiras = models.DecimalField(
        max_digits=10, decimal_places=2)
    corretagem_indice_futuro = models.DecimalField(
        max_digits=10, decimal_places=2)
    corretagem_dolar_futuro = models.DecimalField(
        max_digits=10, decimal_places=2)

    def __str__(self):
        return f"taxas ID: {self.taxas_id} - {self.user.email}"
