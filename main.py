'''
Название блюда
Количество ингредиентов в блюде
Название ингредиента | Количество | Единица измерения
Название ингредиента | Количество | Единица измерения'''


from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = f.readline().strip()
        ingredients_count = int(f.readline().strip())
        ingredients = []
        for i in range(ingredients_count):
            ingrd = f.readline().strip()
            ingredient_name, quantity, measure = ingrd.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure})
        cook_book[dish_name] = ingredients
pprint(cook_book, width=100, sort_dicts=False)