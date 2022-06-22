from django.shortcuts import render, redirect
from .models import Lista
from django.contrib import messages


def index(request):
    

    enderecos = Lista.objects.all()

    dados = {
        'enderecos' : enderecos
    }


    return render(request,'index.html', dados)

def adicionar(request):
    municipios = [
      'RO','AC','AM','RR','PA','AP','TO','MA','PI','CE','RN','PB','PE','AL',
      'SE','BA','MG','ES','RJ','SP','PR','SC','RS','MS','MT','GO','DF'
    ]

    dados = {
        'municipios' : municipios
    }

    return render(request ,'adicionarItem.html', dados)

def cadastrar_endereco(request):
    if request.method == 'POST':
      busca = Lista.objects.filter(cep=request.POST['cep'])
      if busca.exists():
        msg = 'Cadastro atualizado com sucesso!'
        lista = busca[0]
      else:
        msg = 'Cadastro realizado com sucesso!'
        lista = Lista()
      lista.endereco = request.POST['endereco']
      lista.bairro = request.POST['bairro']
      lista.cep = request.POST['cep']
      lista.numero = request.POST['numero']
      lista.uf = request.POST['uf']
      lista.cidade = request.POST['cidade']
      lista.complemento = request.POST['complemento']
      lista.descricao = request.POST['descricao']
      messages.success(request, msg)
      return redirect('index')
    else:  
      return render(request ,'index.html')

def remover_endereco(request, id):
  if request.method == 'GET':
    busca = Lista.objects.filter(id=id)
    if busca.exists():
      lista = busca[0]
      lista.delete()
      messages.success(request, 'Cadastro removido com sucesso!')
      return redirect('index')
    else:
      messages.error(request, 'Não foi possivel encontrar o cadastro a se remover')
    return redirect('index')
  else:  
    return render(request ,'index.html')

