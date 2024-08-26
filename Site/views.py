from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "login.html")

def Cadastro(request):
    return render(request, "cadastro.html")

def VizEstoque(request):
    return render(request, "VisualizarEstoque.html")

def Login(request):
    return render(request, "login.html")

