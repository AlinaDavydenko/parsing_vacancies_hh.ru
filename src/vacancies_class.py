import requests

from src.parsing_class import Parsing


class Vacancies:
    city: str
    number_of_city: int
    vacancy: str
    page: str
    access_token = Parsing.get_access_token

    def __init__(self, city, number_of_city, vacancy, page):
        self.city = city
        self.number_of_city = number_of_city
        self.vacancy = vacancy
        self.page = page

    def get_vacancies(self, access_token):
        """ Функция для получения вакансий """
        url = "https://api.hh.ru/vacancies"
        # настройка параметров
        params = {
            'text': f"{self.vacancy} {self.city}",
            'area': 1,
            'specialization': {self.number_of_city},
            'per_page': 100,
            'page': self.page
        }
        # отправка заголовка
        headers = {'Authorization': f'Bearer {access_token}'}
        data = requests.get(url, params=params, headers=headers)  # запрос с заголовком
        data.raise_for_status()
        return data.json()
