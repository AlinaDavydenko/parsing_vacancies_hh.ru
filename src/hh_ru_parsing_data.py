import requests

from src.abstract_classes import ParsingData


class HeadHunterAPI(ParsingData):
    """ класс для парсинга данных о вакансиях """

    city: str
    number_of_city: int
    page: int
    vacancy: str
    params: dict

    url = "https://api.hh.ru/vacancies"

    def __init__(self, city, number_of_city, page, vacancy):
        self.city = city
        self.number_of_city = number_of_city
        self.page = page
        self.vacancy = vacancy
        self.params = self.get_params()

    def get_params(self):
        params = {
            'text': f"{self.vacancy} {self.city}",
            'area': 1,
            'specialization': {self.number_of_city},
            'per_page': 100,
            'page': self.page
        }
        return params

    @classmethod
    def get_url(cls):
        return cls.url

    def parsing_data(self):
        data = requests.get(url=self.get_url(), params=self.params)
        if data.status_code == 200:
            return data.json()
        else:
            return f'Ошибка {data.status_code}'


# hh_vacancies = HeadHunterAPI('Moscow', 1, 1, 'Developer')
# hh_vacancies.get_params()
# data_set_vacancy = hh_vacancies.parsing_data()
# print(data_set_vacancy)

