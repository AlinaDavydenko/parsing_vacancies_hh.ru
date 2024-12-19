import requests


import os
from dotenv import load_dotenv
load_dotenv()


client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URI')

def get_auth_code():
    """получение ссылки, на которую надо перейти для копирования auth_code"""
    url_for_code = f'https://hh.ru/oauth/authorize?response_type=code&client_id={client_id}'
    return url_for_code


def get_token():
    """ получение токена """
    redirect_uri = 'https://github.com/AlinaDavydenko/parsing_vacancies_hh.ru'
    auth_code = 'UH51LESVF3M6VUI45AM56G89N5D2POCIM47RA9F9IV5HA2PDO5H0FP6664R8RL99'

    oauth_url = "https://hh.ru/oauth/token"
    body = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code,
        'redirect_uri': redirect_uri
        }

    response = requests.post(oauth_url, data=body)
    if response.status_code == 200:
        tokens = response.json()  # получаем токен
        return tokens
    else:
        return f"Request failed with status code: {response.status_code}"


def get_access_token(tokens):
    """ получение access_token """
    access_token = tokens['access_token']
    return access_token


def get_vacancies(city, number_of_city, vacancy, page, access_token):
    """ Функция для получения вакансий """
    url = "https://api.hh.ru/vacancies"
    # настройка параметров
    params = {
        'text': f"{vacancy} {city}",
        'area': 1,
        'specialization': {number_of_city},
        'per_page': 100,
        'page': page
    }
    # отправка заголовка
    headers = {'Authorization': f'Bearer {access_token}'}
    data = requests.get(url, params=params, headers=headers)  # запрос с заголовком
    data.raise_for_status()
    return data.json()


# получаем ссылку
# ssilka = get_auth_code()
# print(ssilka)

# получение токена
# tokens_ = get_token()
# print(tokens_)

# vacanc = get_vacancies('Москва', 1, 'Python', 1, 'USERPFE91TI1JRUMDN24S7G7SJ9LTQSHSP00LC313UIIVD0QVRUOGJQLOPKRBBV2')
# pprint.pp(vacanc)
# print(vacanc)