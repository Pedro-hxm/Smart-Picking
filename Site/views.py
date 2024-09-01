from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request, "login.html")

def Cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get('name')
        email = request.POST.get('email')
        matricula = request.POST.get('matricula')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).exists()

        if user:
            messages.error(request, "Este Usuário já está Cadastrado.")
            return render(request, "cadastro.html")
        
        user = User.objects.create_user(username=username, email=email, first_name=matricula, password=senha)

        messages.success(request ,'Usuário Cadastrado com Sucesso.' )
        return render(request, "login.html")

def VizEstoque(request):
    return render(request, "VisualizarEstoque.html")
# esta com um erro (Corrigir!)
def Login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = authenticate(email=email, password=senha)

        if user: 
            return render(request, 'dadosDaEmpresa.html')
        else:
            messages.error(request, "Email ou senha incorretos.")
            return render(request, 'login.html')
        


def GuiRatão(request):
    return render(request, 'guiratao.html')
