from django.urls import path
from .views import home
from . import views

urlpatterns = [
    # path('', home),
    path('Cadastro/', views.Cadastro, name="Cadastro"),
    # path('VizEstoque/', views.VizEstoque, name="VizEtoque")
    path('Login/', views.Login, name="Login"),
]