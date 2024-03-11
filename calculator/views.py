from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe(request, dish):
    quantity = int(request.GET.get('servings', 1))
    
    if dish in DATA:  # Проверяем, существует ли 'dish' в словаре DATA
        ordered_dish = DATA[dish]
        total_ordered_dish = {}
        
        for ingredient, amount in ordered_dish.items():
            total_ordered_dish[ingredient] = round(amount * quantity, 2)
            
        context = {'recipe': total_ordered_dish, 'dish': dish, 'quantity': quantity}
        return render(request, 'calculator/index.html', context)
    else:
        message = 'Рецепт не найден'  # В случае если 'dish' не существует в словаре DATA
        return HttpResponse(message)







