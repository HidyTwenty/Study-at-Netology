import requests
from bs4 import BeautifulSoup
import json

vacancies = []

def get_vacancies():
    i = 0
    url = f"https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page={i}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    while response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        main_content = soup.find('main', {'class', 'vacancy-serp-content'})
        get_info_in_vacancy(main_content, vacancies)
        i = i + 1
        url = f"https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page={i}"
        response = requests.get(url, headers=headers)
    write_to_json(vacancies)
    return vacancies


def get_info_in_vacancy(main_content, vacancies):
    for vacancy in main_content.find_all('div', {'class': 'serp-item'}):
            item_body__main_info = vacancy.find('div', {'class': 'vacancy-serp-item-body__main-info'})
            item_title = item_body__main_info.find('a', {'class': 'serp-item__title'}).text
            item_href = item_body__main_info.find('a', {'class': 'serp-item__title'})['href']
            item_salary = get_salary(item_body__main_info)
            item_company = get_company(item_body__main_info)
            item_city = get_city(item_body__main_info)
            append_vacancies(item_title, item_href, item_salary, item_company, item_city, vacancies)
            


def append_vacancies(item_title, item_href, item_salary, item_company, item_city, vacancies):
    if 'django' in item_title.lower() or 'flask' in item_title.lower():
        my_dict = {item_title: (item_href, item_salary, item_company, item_city)}
        vacancies.append(my_dict)


def get_salary(item_body__main_info):
    item_salary_info = item_body__main_info.find('span', class_='bloko-header-section-3')
    if item_salary_info is None:
        return 'Зарплата не указана'
    else:
        salary_text = ' '.join(item_salary_info.stripped_strings).replace('\u202f', ' ')
        return salary_text


def get_city(item_body__main_info):
    vacancy_info = item_body__main_info.find('div', {'class': 'vacancy-serp-item__info'})
    city = vacancy_info.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text.split()[0].rstrip(',.')
    return city


def get_company(item_body__main_info):
    vacancy_info = item_body__main_info.find('div', {'class': 'vacancy-serp-item__info'})
    company_name = vacancy_info.find('a', {'class': 'bloko-link_kind-tertiary'}).text.replace('\xa0', ' ')
    return company_name


def write_to_json(vacancies):
    with open('vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies, f, ensure_ascii=False, indent=4)


print(get_vacancies())