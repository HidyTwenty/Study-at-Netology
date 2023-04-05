queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

result = {}

for query in queries:
    words = query.split()

    if len(words) in result.keys():
        result[len(words)] = result[len(words)] + 1
    else:
        result.update({
            len(words): 1
        })

for key, value in result.items():
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов из {key} слов - {percentage}%')