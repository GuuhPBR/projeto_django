from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("adicionarItem", views.adicionar, name='adicionarItem'),
    path("cadastrar_endereco", views.cadastrar_endereco, name="cadastrar_endereco"),
    path("remover_endereco/<int:id>", views.remover_endereco, name="remover_endereco")
]