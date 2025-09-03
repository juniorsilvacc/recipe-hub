from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'home.html', {'recipes': recipes})


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True,).order_by('-id')
    return render(request, 'category.html', {'recipes': recipes})


def recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if not recipe:
        raise Http404("Receita não encontrada")
    return render(request, 'recipe.html', {'recipe': recipe})


