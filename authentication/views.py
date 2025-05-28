from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm
from .models import RegistrationKey


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            remember_me = form.cleaned_data.get("remember_me")

            if user is not None:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(3600 * 24 * 7)  # 7 dias
                else:
                    # Expira no fechamento do navegador
                    request.session.set_expiry(0)
                return redirect("/app/")
            else:
                msg = 'Credenciais inválidas. Tente novamente.'
        else:
            msg = 'Erro ao validar o formulário.'

    return render(request, "auth/login.html", {"form": form, "msg": msg})


def logout_view(request):
    logout(request)  # Finaliza a sessão do usuário
    # Redireciona para a página de login ou outra página
    return redirect('authentication:login')


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Salva o usuário sem gravar no banco ainda
            user = form.save(commit=False)
            user.username = user.email  # Define o email como username
            user.save()  # Agora salva no banco

            # Marcar a chave como usada
            key = form.cleaned_data.get('key')
            reg_key = RegistrationKey.objects.get(key=key)
            reg_key.is_used = True
            reg_key.save()

            raw_password = form.cleaned_data.get("password1")
            # Autentica com email
            user = authenticate(email=user.email, password=raw_password)

            msg = 'Usuário criado com sucesso, faça o <a href="/auth/login">login</a>.'
            success = True
        else:
            msg = 'O formulário contém erros. Verifique os campos e tente novamente.'
    else:
        form = SignUpForm()

    return render(request, "auth/cadastrar.html", {"form": form, "msg": msg, "success": success})
