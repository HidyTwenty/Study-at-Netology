def count_words(queries):
    result = {}
    for query in queries:
        words = query.split()

        if len(words) in result.keys():
            result[len(words)] = result[len(words)] + 1
        else:
            result.update({
                len(words): 1
            })
    return result

def calculate_percentage(result, total_queries):
    percentage_results = {}
    for key, value in result.items():
        percentage = round((value / total_queries) * 100, 2)
        percentage_results[key] = percentage
    return percentage_results

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

word_count_result = count_words(queries)
percentage_result = calculate_percentage(word_count_result, len(queries))

for key, value in percentage_result.items():
    print(f'Поисковых запросов из {key} слов - {value}%')