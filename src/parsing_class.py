import requests

import os

from dotenv import load_dotenv

load_dotenv()


class Parsing:
    """ класс для парсинга данных о вакансиях """
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    redirect_uri = os.getenv('REDIRECT_URI')

    def __init__(self, redirect_uri, auth_code, client_id, client_secret, tokens, access_token):
        self.redirect_uri = redirect_uri
        self.auth_code = auth_code
        self.client_id = client_id
        self.client_secret = client_secret
        self.tokens = tokens
        self.access_token = access_token

    def get_auth_code(self):
        """получение ссылки, на которую надо перейти для копирования auth_code"""
        url_for_code = f'https://hh.ru/oauth/authorize?response_type=code&client_id={self.client_id}'
        return url_for_code

    @property
    def get_token(self):
        """ получение токена """
        redirect_uri = 'https://github.com/AlinaDavydenko/parsing_vacancies_hh.ru'
        auth_code = 'UH51LESVF3M6VUI45AM56G89N5D2POCIM47RA9F9IV5HA2PDO5H0FP6664R8RL99'

        oauth_url = "https://hh.ru/oauth/token"
        body = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': auth_code,
            'redirect_uri': redirect_uri
        }

        response = requests.post(oauth_url, data=body)
        if response.status_code == 200:
            self.tokens = response.json()  # получаем токен
            return self.tokens
        else:
            return f"Request failed with status code: {response.status_code}"

    @property
    def get_access_token(self):
        """ получение access_token """
        self.access_token = self.tokens['access_token']
        return self.access_token


