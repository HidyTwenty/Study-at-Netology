import requests
from bs4 import BeautifulSoup
import json


def fetch_vacancies_page(page_number):
    url = f"https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page={page_number}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    return requests.get(url, headers=headers)


def extract_vacancies(soup):
    main_content = soup.find('main', {'class', 'vacancy-serp-content'})
    return main_content.find_all('div', {'class': 'serp-item'})


def extract_vacancy_info(vacancy):
    info = vacancy.find('div', {'class': 'vacancy-serp-item-body__main-info'})
    title = info.find('a', {'class': 'serp-item__title'}).text
    href = info.find('a', {'class': 'serp-item__title'})['href']
    salary = extract_salary(info)
    company = extract_company(info)
    city = extract_city(info)
    return title, href, salary, company, city


def extract_salary(info):
    salary_info = info.find('span', class_='bloko-header-section-3')
    if salary_info is None:
        return 'Зарплата не указана'
    else:
        return ' '.join(salary_info.stripped_strings).replace('\u202f', ' ')


def extract_city(info):
    vacancy_info = info.find('div', {'class': 'vacancy-serp-item__info'})
    return vacancy_info.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).text.split()[0].rstrip(',.')


def extract_company(info):
    vacancy_info = info.find('div', {'class': 'vacancy-serp-item__info'})
    return vacancy_info.find('a', {'class': 'bloko-link_kind-tertiary'}).text.replace('\xa0', ' ')


def append_vacancy(vacancies, title, href, salary, company, city):
    if 'django' in title.lower() or 'flask' in title.lower():
        vacancies.append({title: (href, salary, company, city)})


def write_vacancies_to_json(vacancies):
    with open('vacancies.json', 'w', encoding='utf-8') as f:
        json.dump(vacancies, f, ensure_ascii=False, indent=4)


def get_vacancies():
    vacancies = []
    page_number = 0

    while True:
        response = fetch_vacancies_page(page_number)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        vacancies_list = extract_vacancies(soup)

        for vacancy in vacancies_list:
            title, href, salary, company, city = extract_vacancy_info(vacancy)
            append_vacancy(vacancies, title, href, salary, company, city)

        page_number += 1

    write_vacancies_to_json(vacancies)
    return vacancies


print(get_vacancies())