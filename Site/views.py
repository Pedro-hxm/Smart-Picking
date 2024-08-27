from django.http import HttpResponse
from django.shortcuts import render

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
        return HttpResponse(username)

def VizEstoque(request):
    return render(request, "VisualizarEstoque.html")

def Login(request):
    return render(request, "login.html")

def GuiRatão(request):
    return render(request, 'guiratao.html')
