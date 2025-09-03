from django.http import Http404
from django.shortcuts import render, get_list_or_404
from recipes.models import Recipe


def home(request):
    """Exibe todas as receitas publicadas na página inicial"""
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'home.html', {'recipes': recipes})


def category(request, category_id):
    """Exibe todas as receitas de uma categoria específica"""
    recipes = get_list_or_404(
            Recipe.objects.filter(
            category__id=category_id,  # busca pelo ID da categoria
            is_published=True,         # somente receitas publicadas
        ).order_by('-id')              # ordena por ID decrescente, mostrando as mais recentes primeiro
    )

    # Renderiza o template 'category.html', passando o contexto com as receitas filtradas
    return render(request, 'category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    """Exibe os detalhes de uma receita específica"""
    recipe = Recipe.objects.get(id=id)

    if not recipe:
        raise Http404("Receita não encontrada")
    
    return render(request, 'recipe.html', {'recipe': recipe})


