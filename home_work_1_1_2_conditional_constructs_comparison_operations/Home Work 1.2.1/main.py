region = 'none'
percent = 2
children = int(0)
salary_project = 'none'
insurance = 'none'

region = input('Из какого Вы региона? ')

if region == 'Амур' or region == 'Бурятия' or region == 'ЕАО' or region == 'Забайкал' or region == 'Камчатка' or region == 'Магадан' or region == 'Приморск' or region == 'Якутия' or region == 'Сахалин' or region == 'Хабаровск' or region == 'Чукотка':

  children = int(input('Сколько у Вас детей? '))
  if children >= 3:
    percent = percent - 1
  else:
    percent = percent

  salary_project = input('Есть ли у Вас зарплатный проект в нашем банке? ')
  if salary_project == 'да' or salary_project == 'Да' or salary_project == 'ДА':
    percent = percent - 0.5
  else:
    percent = percent
    
  insurance = input('Хотите ли Вы оформить страховку? ')
  if insurance == 'да' or insurance == 'Да' or insurance == 'ДА':
    percent = percent - 1.5
  else:
    percent = percent
  print('Ваш итоговый процент по ипотеке составляет:', percent, '%')

else:
  print('К сожалению мы работаем только с регионами из дальнего востока.')