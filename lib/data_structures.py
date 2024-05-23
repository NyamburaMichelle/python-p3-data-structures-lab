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
     names = [food["name"] for food in spicy_foods]
     return names

names = get_names(spicy_foods)

#print(names)


def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

#print(get_spiciest_foods(spicy_foods))




def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]

        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

#print_spicy_foods(spicy_foods)






def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] ==cuisine:
            return food
    
#print(get_spicy_food_by_cuisine(spicy_foods, "American"))




def print_spiciest_foods(spicy_foods):
     spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
     for food in spiciest_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

print(print_spiciest_foods(spicy_foods))







def get_average_heat_level(spicy_foods):
     total_heat_level = sum(food["heat_level"] for food in spicy_foods)
     num_spicy_foods = len(spicy_foods)
    
     if num_spicy_foods == 0:
        return 0  
    
     return total_heat_level / num_spicy_foods

print(get_average_heat_level(spicy_foods))






def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

spicy_food = {"name": "Tofu", "cuisine": "Sichu", "heat_level": 5}

print(create_spicy_food(spicy_foods,spicy_food))