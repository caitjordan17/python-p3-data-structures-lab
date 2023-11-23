spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [item["name"] for item in spicy_foods]

def get_spiciest_foods(spicy_foods):
    heat_array = []
    for item in spicy_foods:
        if item["heat_level"] > 5:
            heat_array.append(item)
    
    return heat_array

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_average_heat_level(spicy_foods):
    heat = []
    for food in spicy_foods:
        heat.append(food["heat_level"])
    return sum(heat) / len(heat)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


    # max_heat = max([item["heat_level"] for item in spicy_foods])
    # for item in spicy_foods:
    #     if item["heat_level"] == max_heat:
    #         return item