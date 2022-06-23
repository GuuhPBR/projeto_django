# Projeto de cadastro de endereço 

## Linguagen/framework

Este projeto foi criado usando 
- [Django v4.0.5](https://www.djangoproject.com/).
- [Python v3.9.2](https://www.python.org/).
- [Jquery v2.2.4](https://jquery.com/).
- [Bootstrap v5.2.0](https://getbootstrap.com/).

## Banco de dados
- [Postgres v6.8](https://www.postgresql.org/).

A configuração padrão do banco esta definida da seguinte forma:
```
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lista_enderecos',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost'
    }
```

## DER cadastro de endereços
![cadastro_endereco_lista](https://user-images.githubusercontent.com/80047895/175180996-a32e7d80-63fe-4d98-9471-3636ceb3f219.PNG)


Mas fique a vontade para definir as credenciais conforme desejar

## Scripts adicionais

Dentro do projeto, para inicia-lo, você deve executar os seguintes comandos:
#### iniciar web server
 ```
 python manage.py runserver
 ```

 #### com database ( lista_enderecos ) criado execute o comando
 ```
 python manage.py makemigrations
 python manage.py migrate
 ```


#### Aplicação rodando
Depois que a aplicação estiver iniciado, você deve abrir o seguinte endereço abaixo no seu navegador:
[http://localhost:8000](http://localhost:8000) 

Você também poderá acompanhar os erros e requisições em seu terminal
