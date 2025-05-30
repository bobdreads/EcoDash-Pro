from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Para feedback ao usuário
from .forms import OperacaoForm

# Create your views here.


@login_required(login_url="/auth/login/")
def index(request):
    return render(request, 'index.html')


def trades(request):
    if request.method == 'POST':
        # Se o formulário foi enviado
        form = OperacaoForm(request.POST)
        if form.is_valid():
            # Formulário é válido, podemos processar os dados
            # Cria o objeto Operacao mas não salva no BD ainda
            operacao = form.save(commit=False)
            operacao.user = request.user       # Associa o usuário logado
            operacao.save()                    # Agora salva no BD!

            # Mensagem de sucesso
            messages.success(request, 'Trade registrado com sucesso!')
            # Redireciona para a mesma página (ou outra, ex: 'index')
            return redirect('trades')
        else:
            # Formulário inválido, exibe mensagens de erro
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        # Se for um GET request, apenas mostra o formulário em branco
        form = OperacaoForm()

    context = {
        'form': form
    }
    return render(request, 'trades.html', context)
