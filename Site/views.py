from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

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

        user = User.objects.filter(username=username).first()
        
        if user: 
            return HttpResponse("Esse Usuario j´s existe.")
            # messages.error(request, 'Usuário já existe.')

        return HttpResponse(username)

def VizEstoque(request):
    return render(request, "VisualizarEstoque.html")

def Login(request):
    return render(request, "login.html")

def GuiRatão(request):
    return render(request, 'guiratao.html')
