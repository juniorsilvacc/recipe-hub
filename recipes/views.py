from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    receitas = [
        {
            "id": 1,
            "title": "Bolo de Cenoura",
            "description": "Um delicioso bolo de cenoura fofinho com cobertura de chocolate.",
            "preparation_time": 45,
            "preparation_time_unit": "minutos",
            "servings": 8,
            "servings_unit": "fatias",
            "preparation_steps": [
                "Bater a cenoura, ovos e óleo no liquidificador.",
                "Misturar com açúcar e farinha em uma tigela.",
                "Adicionar fermento e mexer delicadamente.",
                "Levar ao forno a 180°C por 40 minutos.",
                "Preparar a cobertura de chocolate e espalhar por cima."
            ],
            "created_at": "2025-09-01T10:30:00",
            "author": {
                "first_name": "Maria",
                "last_name": "Souza"
            },
            "category": {
                "name": "Sobremesas"
            },
            "cover": "https://www.coisasdaleia.com.br/wp-content/uploads/2023/03/bolo-de-cenoura-liquidificador-1.jpg"
        },
         {
            "id": 2,
            "title": "Lasanha à Bolonhesa",
            "description": "Lasanha com molho bolonhesa caseiro e muito queijo.Lasanha com molho bolonhesa caseiro e muito queijo.",
            "preparation_time": 90,
            "preparation_time_unit": "minutos",
            "servings": 6,
            "servings_unit": "porções",
            "preparation_steps": [
                "Preparar o molho bolonhesa com carne moída e tomate.",
                "Cozinhar a massa da lasanha.",
                "Montar em camadas de molho, massa e queijo.",
                "Assar no forno a 200°C por 30 minutos."
            ],
            "created_at": "2025-09-01T11:00:00",
            "author": {
                "first_name": "João",
                "last_name": "Pereira"
            },
            "category": {
                "name": "Massas"
            },
            "cover": "https://swiftbr.vteximg.com.br/arquivos/ids/207917-768-768/618352-lasanha-a-bolonhesa_rec.jpg?v=638852197178600000"
        },
         {
            "id": 3,
            "title": "Lasanha à Bolonhesa",
            "description": "Lasanha com molho bolonhesa caseiro e muito queijo.Lasanha com molho bolonhesa caseiro e muito queijo.",
            "preparation_time": 90,
            "preparation_time_unit": "minutos",
            "servings": 6,
            "servings_unit": "porções",
            "preparation_steps": [
                "Preparar o molho bolonhesa com carne moída e tomate.",
                "Cozinhar a massa da lasanha.",
                "Montar em camadas de molho, massa e queijo.",
                "Assar no forno a 200°C por 30 minutos."
            ],
            "created_at": "2025-09-01T11:00:00",
            "author": {
                "first_name": "João",
                "last_name": "Pereira"
            },
            "category": {
                "name": "Massas"
            },
            "cover": "https://swiftbr.vteximg.com.br/arquivos/ids/207917-768-768/618352-lasanha-a-bolonhesa_rec.jpg?v=638852197178600000"
        }
    ]

    return render(request, 'home.html', {'receitas': receitas})


def recipe(request, id):
    return HttpResponse(f'Receita de ID {id}')
