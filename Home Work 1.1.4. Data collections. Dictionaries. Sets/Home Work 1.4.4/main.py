stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
result = ''
i = 0

for key, value in stats.items():
  if value > i:
    i = value
    result = key
  elif value == i:
    result = result + ', ' + key

print(result)