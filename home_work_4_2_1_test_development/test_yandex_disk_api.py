import os
import requests
from random import randint
import pytest

API_BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'
API_KEY = 'ввести свой API KEY'


@pytest.fixture(scope='module')
def session():
    with requests.Session() as s:
        s.headers.update({'Authorization': f'OAuth {API_KEY}'})
        yield s


def test_create_folder_positive(session):
    folder_name = f'test_folder_{randint(1000, 9999)}'
    response = session.put(f'{API_BASE_URL}?path={folder_name}')

    assert response.status_code == 201, f'Ожидаемый статус код 201, но получили {response.status_code}'

    check_folder_response = session.get(f'{API_BASE_URL}?path={folder_name}')
    assert check_folder_response.status_code == 200, f'Ожидаемый статус код 200, но получили {check_folder_response.status_code}'
    assert check_folder_response.json()['name'] == folder_name, f"Ожидаемое название папки '{folder_name}', но получили '{check_folder_response.json()['name']}'"

    session.delete(f'{API_BASE_URL}?path={folder_name}')


def test_create_folder_already_exists(session):
    folder_name = f'test_folder_{randint(1000, 9999)}'
    session.put(f'{API_BASE_URL}?path={folder_name}')

    response = session.put(f'{API_BASE_URL}?path={folder_name}')
    assert response.status_code == 409, f'Ожидаемый статус код 409, но получили {response.status_code}'

    session.delete(f'{API_BASE_URL}?path={folder_name}')


def test_create_folder_invalid_path(session):
    folder_name = f':test_folder_{randint(1000, 9999)}'
    response = session.put(f'{API_BASE_URL}?path={folder_name}')

    assert response.status_code == 400, f'Ожидаемый статус код 400, но получили {response.status_code}'
