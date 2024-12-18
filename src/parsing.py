import requests
import json

client_id = 'UT6CH9LEKVBG3DDPEHVU0JFJBOKLQ1QQKNU8COQA0P2DVRLAHB9TU1MUVN8OSKKH'
client_secret = 'IAQ1FSQKE7MEIEPIPCV6RTK5UAHTJ7TEG0DQDQEOM9GCM8TNRAPLFG073AI1KNLF'

REDIRECT_URI = ''
state_value = ''


def get_auth_code():
    """получение ссылки, на которую надо перейти для копирования auth_code"""
    url_for_code = f'https://hh.ru/oauth/authorize?response_type=code&client_id={client_id}'
    return url_for_code


def get_token():
    """ получение токена """
    redirect_uri = 'https://github.com/AlinaDavydenko/parsing_vacancies_hh.ru'
    auth_code = 'IBH00RN40NRINM7SQ2VMLN63BOL50ALGHPFHN47UGRABKUS98G01IRP8SV9I4MQ5'

    oauth_url = "https://hh.ru/oauth/token"
    body = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code,
        'redirect_uri': redirect_uri
    }

    response = requests.post(oauth_url, data=body)

    tokens = response.json()  # получаем токен
    return tokens


def get_data_from_tokens(tokens):
    """ получение данных с tokens """
    access_token = tokens['access_token']
    token_type = tokens['token_type']
    refresh_token = tokens['refresh_token']
    expires_in = tokens['expires_in']
    return access_token, token_type, refresh_token, expires_in


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
ssilka = get_auth_code()
print(ssilka)

# получение токена
# tokens_ = get_token()
# print(tokens_)

# get_tokens = get_access_token(tokens_)
# print(get_tokens)
vacanc = get_vacancies('Москва', 1, 'Python', 1, 'USERPFE91TI1JRUMDN24S7G7SJ9LTQSHSP00LC313UIIVD0QVRUOGJQLOPKRBBV2')
print(vacanc)
