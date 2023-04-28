import pytest
from home_work_1_4_1.main import select_russia

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
class TestSelectRussia:
    def test_select_russia(self):
        a1 = geo_logs
        result = select_russia(a1)
        expected = [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}]
        assert result == expected










from home_work_1_4_2.main import count_words_percentage

@pytest.mark.parametrize("input_ids, expected_output", [
    ({
         'user1': [213, 213, 213, 15, 213],
         'user2': [54, 54, 119, 119, 119],
         'user3': [213, 98, 98, 35]
     }, [213, 15, 54, 119, 98, 35]),
    ({
         'user1': [1, 1, 1, 2, 2],
         'user2': [2, 3, 3, 3, 3],
         'user3': [1, 4, 4, 5]
     }, [1, 2, 3, 4, 5]),
    ({
         'user1': [],
         'user2': [],
         'user3': []
     }, []),
])
def test_count_words_percentage(input_ids, expected_output):
    assert count_words_percentage(input_ids) == expected_output










from home_work_1_4_3.main import count_words, calculate_percentage

@pytest.mark.parametrize("queries, expected", [
    ([
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ], {3: 4, 2: 3}),
    ([
        'новости спорта',
        'курс доллара',
        'курс по питону'
    ], {2: 2, 3: 1}),
    ([], {}),
])
def test_count_words(queries, expected):
    assert count_words(queries) == expected

@pytest.mark.parametrize("result, total_queries, expected", [
    ({3: 4, 2: 3}, 7, {3: 57.14, 2: 42.86}),
    ({2: 2, 3: 1}, 3, {2: 66.67, 3: 33.33}),
    ({}, 0, {}),
])
def test_calculate_percentage(result, total_queries, expected):
    assert calculate_percentage(result, total_queries) == expected