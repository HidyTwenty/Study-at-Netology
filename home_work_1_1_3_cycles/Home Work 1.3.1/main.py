boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()

number_of_boys = len(boys)
number_of_girls = len(girls)

if number_of_boys == number_of_girls:
  print('Идеальные пары:')
  for boy, girl in zip(boys, girls):   
    print(boy, 'и', girl)
else:
  print('Количество мальчиков и девочек отличается. Кто-то может остаться без пары. Пожалуйста, измените списки.')