square_length = int(input('Введите длину стороны квадрата: '))
square_perimetr = 4 * square_length
area_of_a_square = square_length * square_length
print('\n')
print('Периметр: ', square_perimetr)
print('Площадь: ', area_of_a_square)
print('\n')

rectangle_length = int(input('Введите длину прямоугольника: '))
rectangle_width = int(input('Введите ширину прямоугольника: '))
rectangle_perimetr = 2 * (rectangle_length + rectangle_width)
area_of_a_rectangle = rectangle_length * rectangle_width
print('\n')
print('Периметр: ', rectangle_perimetr)
print('Площадь: ', area_of_a_rectangle)
print('\n')

user_separator = input('Введите символ для разделения: ')
print('\n')
print(user_separator * (square_perimetr + area_of_a_rectangle))
print('\n')

salary = int(input('Введите заработную плату в месяц: '))
for_a_mortgage = int(input('Введите, какой процент(%) уходит на ипотеку: '))
for_life = int(input('Введите, какой процент(%) уходит на жизнь: '))
spent_on_mortgage = int(salary * (for_a_mortgage / 100))
spent_on_life = int(salary * (for_life / 100))
accumulated = salary - (spent_on_mortgage + spent_on_life)
print('\n')
print('На ипотеку было потрачено: ', spent_on_mortgage * 12)
print('Было накоплено: ', accumulated * 12)