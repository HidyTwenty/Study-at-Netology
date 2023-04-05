month = input('Введите месяц: ')
date = int(input('Введите дату: '))

if month == 'март' and date >= 21 and date <= 31:
  print('Овен')
elif month == 'апрель' and date >= 1 and date <= 20:
  print('Овен')
elif month == 'апрель' and date >= 21 and date <= 30:
  print('Телец')
elif month == 'май' and date >= 1 and date <= 21:
  print('Телец')
elif month == 'май' and date >= 22 and date <= 31:
  print('Близнецы')
elif month == 'июнь' and date >= 1 and date <= 21:
  print('Близнецы')
elif month == 'июнь' and date >= 22 and date <= 30:
  print('Рак')
elif month == 'июль' and date >= 1 and date <= 22:
  print('Рак')
elif month == 'июль' and date >= 23 and date <= 31:
  print('Лев')
elif month == 'август' and date >= 1 and date <= 21:
  print('Лев')
elif month == 'август' and date >= 22 and date <= 31:
  print('Дева')
elif month == 'сентябрь' and date >= 1 and date <= 23:
  print('Дева')
elif month == 'сентябрь' and date >= 24 and date <= 30:
  print('Весы')
elif month == 'октябрь' and date >= 1 and date <= 23:
  print('Весы')
elif month == 'октябрь' and date >= 24 and date <= 31:
  print('Скорпион')
elif month == 'ноябрь' and date >= 1 and date <= 22:
  print('Скорпион')
elif month == 'ноябрь' and date >= 23 and date <= 30:
  print('Стрелец')
elif month == 'декабрь' and date >= 1 and date <= 22:
  print('Стрелец')
elif month == 'декабрь' and date >= 23 and date <= 31:
  print('Козерог')
elif month == 'январь' and date >= 1 and date <= 20:
  print('Козерог')
elif month == 'январь' and date >= 21 and date <= 31:
  print('Водолей')
elif month == 'февраль' and date >= 1 and date <= 19:
  print('Водолей')
elif month == 'февраль' and date >= 20 and date <= 29:
  print('Рыбы')
elif month == 'март' and date >= 1 and date <= 20:
  print('Рыбы')
else:
  print('Некорректная дата или месяц.')