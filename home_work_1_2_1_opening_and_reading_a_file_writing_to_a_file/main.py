def get_recipes():
    cook_book = {}
    with open('2.4.files/recipes.txt', 'r', encoding='utf8') as recipes:
        for line in recipes:
            dish_name = line.strip()
            cook_book[dish_name] = []
            quantity_of_ingredients = recipes.readline()
            for i in range(int(quantity_of_ingredients)):
                ingredients = recipes.readline()
                ingredient_name, quantity, measure = ingredients.split(" | ")
                cook_book[dish_name].append({'ingredient_name': ingredient_name.rstrip(),
                                            'quantity': int(quantity.replace(' ', '')),
                                            'measure': measure.rstrip().replace(' ', '')})
            recipes.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in get_recipes().keys():
            for ingredients in get_recipes()[dish]:
                if ingredients['ingredient_name'] not in shop_list:  
                    ingredient_name = ingredients['ingredient_name']
                    measure = ingredients['measure']
                    quantity = ingredients['quantity']
                    shop_list[ingredient_name] = { 'measure': measure, 'quantity': int(quantity * person_count)}
                else:
                    ingredient_name = ingredients['ingredient_name']
                    quantity = ingredients['quantity']
                    shop_list[ingredient_name]['quantity'] = int(shop_list[ingredient_name]['quantity']) + (int(ingredients['quantity']) * person_count)
    return shop_list

get_recipes()
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))


###################################################################################


txt1 = open('1.txt', encoding="utf8")
txt2 = open('2.txt', encoding="utf8")
txt3 = open('3.txt', encoding="utf8")

number_of_lines1 = 0
number_of_lines2 = 0
number_of_lines3 = 0

for line in txt1:
    number_of_lines1 += 1
for line in txt2:
    number_of_lines2 += 1
for line in txt3:
    number_of_lines3 += 1

if number_of_lines1 > number_of_lines2 & number_of_lines2 > number_of_lines3:
    print(txt1.name)
    print(number_of_lines1)
    txt1 = open('1.txt', encoding="utf8")
    print(txt1.read())
    print(txt2.name)
    print(number_of_lines2)
    txt2 = open('2.txt', encoding="utf8")
    print(txt2.read())
    print(txt3.name)
    print(number_of_lines3)
    txt3 = open('3.txt', encoding="utf8")
    print(txt3.read())
elif number_of_lines1 > number_of_lines3 & number_of_lines3 > number_of_lines2:
    print(txt1.name)
    print(number_of_lines1)
    txt1 = open('1.txt', encoding="utf8")
    print(txt1.read())
    print(txt3.name)
    print(number_of_lines3)
    txt3 = open('3.txt', encoding="utf8")
    print(txt3.read())
    print(txt2.name)
    print(number_of_lines2)
    txt2 = open('2.txt', encoding="utf8")
    print(txt2.read())
elif number_of_lines2 > number_of_lines1 & number_of_lines1 > number_of_lines3:
    print(txt2.name)
    print(number_of_lines2)
    txt2 = open('2.txt', encoding="utf8")
    print(txt2.read())
    print(txt1.name)
    print(number_of_lines1)
    txt1 = open('1.txt', encoding="utf8")
    print(txt1.read())
    print(txt3.name)
    print(number_of_lines3)
    txt3 = open('3.txt', encoding="utf8")
    print(txt3.read())
elif number_of_lines2 > number_of_lines3 & number_of_lines3 > number_of_lines1:
    print(txt2.name)
    print(number_of_lines2)
    txt2 = open('2.txt', encoding="utf8")
    print(txt2.read())
    print(txt3.name)
    print(number_of_lines3)
    txt3 = open('3.txt', encoding="utf8")
    print(txt3.read())
    print(txt1.name)
    print(number_of_lines1)
    txt1 = open('3.txt', encoding="utf8")
    print(txt1.read())
elif number_of_lines3 > number_of_lines1 & number_of_lines1 > number_of_lines2:
    print(txt2.name)
    print(number_of_lines2)
    txt2 = open('2.txt', encoding="utf8")
    print(txt2.read())
    print(txt1.name)
    print(number_of_lines1)
    txt1 = open('1.txt', encoding="utf8")
    print(txt1.read())
    print(txt3.name)
    print(number_of_lines3)
    txt3 = open('3.txt', encoding="utf8")
    print(txt3.read())
else:
    print(txt3.name)
    print(number_of_lines3)
    txt3 = open('3.txt', encoding="utf8")
    print(txt3.read())
    print(txt2.name)
    print(number_of_lines2)
    txt2 = open('2.txt', encoding="utf8")
    print(txt2.read())
    print(txt1.name)
    print(number_of_lines1)
    txt1 = open('3.txt', encoding="utf8")
    print(txt1.read())