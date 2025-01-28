import json

from src.work_with_vacancies import Vacancy

from src.abstract_classes import ABCWorkWithFile


class WorkWithFile(ABCWorkWithFile):
    """ класс для работы с файлами (dataset из класса HeadHunterAPI) """
    info_about_vacancies: list = []

    def __init__(self, path: str = 'data/data.json'):
        self.__path = path
        self.info_about_vacancies = []

    # блок функций для добавления в файлы
    def add_to_file(self, vacancies: list[dict]):
        """ функция добавляет данные формата json в файл"""
        with open(self.__path, 'w', encoding='utf-8') as json_file:
            json.dump(vacancies, json_file, ensure_ascii=False, indent=4)

    # блок функций для чтения из файла
    def read_data_json(self):
        """ чтение json файла """
        try:
            with open(self.__path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            vacancies = []
            for vacancy in data['items']:
                vacancies.append(Vacancy(
                    vacancy['name'],
                    vacancy['apply_alternate_url'],
                    vacancy['salary'],
                    vacancy['area']['name']
                ))

                self.info_about_vacancies = vacancies
        except FileNotFoundError:
            print(f"Файл {self.__path} не найден.")
            self.info_about_vacancies = []

    @classmethod
    def return_vacancies(cls):
        """ чтение json файла """
        return cls.info_about_vacancies

    # удаление данных из файла
    def remove_from_file(self):
        """ функция удаляет данные из файла """
        with open(self.__path, 'w'):
            pass

    def __str__(self):
        return str(getattr(self, 'info_about_vacancies', ''))
