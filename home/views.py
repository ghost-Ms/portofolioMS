import os

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.conf import settings

from home.models import Mensagem


def index(request):
    return render(request, "home/index.html")


def sobre(request):
    return render(request, "home/sobre.html")


def reflexoes(request):
    return render(request, "home/reflexoes.html")


def abrir_pdf(request, nome_arquivo):
    # Caminho para o arquivo PDF
    caminho_pdf = os.path.join(settings.BASE_DIR, 'templates', 'static', 'pdf', nome_arquivo)

    # Verificar se o arquivo existe
    if os.path.exists(caminho_pdf):
        try:
            # Abrir o arquivo PDF
            pdf_file = open(caminho_pdf, 'rb')
            # Retornar o arquivo PDF como uma resposta de arquivo
            return FileResponse(pdf_file)
        except Exception as e:
            # Se ocorrer um erro ao abrir o arquivo, retornar uma resposta de erro
            return HttpResponse(f"Erro ao abrir o arquivo PDF: {e}", status=500)
    else:
        # Retornar uma resposta de erro se o arquivo não for encontrado
        return HttpResponse("Arquivo não encontrado", status=404)


def contacto(request):
    return render(request, "home/contacto.html")


def enviar_mensagem(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        # Salvar na base de dados
        Mensagem.objects.create(nome=nome, email=email, assunto=assunto, mensagem=mensagem)

        # Definir mensagem de sucesso
        messages.success(request, 'A sua mensagem foi enviada com sucesso!')

        # Redirecionar de volta para a página de contato
        return redirect('contacto')
    else:
        # Se o método não for POST, renderize o template do formulário de contato
        return render(request, 'contact_form.html')


