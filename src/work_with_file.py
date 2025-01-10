import json

from src.config import path_to_data_json

from src.hh_ru_parsing_data import HeadHunterAPI

from src.abstract_classes import ABCWorkWithFile

hh_vacancies = HeadHunterAPI('Moscow', 1, 1, 'Developer')
hh_vacancies.get_params()
dataset = hh_vacancies.parsing_data()


class WorkWithFile(ABCWorkWithFile):
    """ класс для работы с файлами (dataset из класса HeadHunterAPI) """
    data_set: dict
    data_json = path_to_data_json
    info_about_vacancies: dict
    list_of_criteria_vacancy: list = []

    def __init__(self, data_set, salary, name_of_vacancy):
        self.data_set = data_set
        # критерии для фильтрации ваканский
        self.salary = salary
        self.name_of_vacancy = name_of_vacancy

    # переопределение
    def set_dataset_for_class(self):
        """ записывет data_set на уровне класса"""
        WorkWithFile.data_set = self.data_set
        print('функция set_dataset_for_class')

    # блок функций для добавления в файлы
    @classmethod
    def add_to_file(cls):
        """ функция добавляет данные формата json в файл"""
        with open(cls.data_json, 'w', encoding='utf-8') as json_file:
            json.dump(cls.data_set, json_file, ensure_ascii=False, indent=4)
        print('функция add_to_file')

    # блок функций для чтения из файла
    # определяем словарь вакансий для класса
    @classmethod
    def read_data_json(cls):
        """ чтение json файла """
        with open(cls.data_json, 'r', encoding='utf-8') as json_file:
            cls.info_about_vacancies = json.load(json_file)
        print(cls.info_about_vacancies)

    @classmethod
    def return_vacancies(cls):
        """ чтение json файла """
        return cls.info_about_vacancies

    # удаление данных из файла
    @classmethod
    def remove_from_file(cls):
        """ функция добавляет данные формата json в файл"""
        with open(cls.data_json, 'w'):
            pass

    # получение данных из файла по критериями
    def get_vacancy_from_file(self):
        """ фильтрация вакансий в списке по критериям """
        # если имя вакансии соответствует заданному, тогда добавляем его в список
        for vacancies in WorkWithFile.info_about_vacancies['items']:
            if (vacancies['name'] == self.name_of_vacancy and vacancies['salary'] is not None and
                    vacancies['salary']['from'] == self.salary):
                WorkWithFile.list_of_criteria_vacancy.append(vacancies)
        return WorkWithFile.list_of_criteria_vacancy

    def __str__(self):
        return str(self.list_of_criteria_vacancy)


a = WorkWithFile(dataset, 400000, 'Финансовый директор')
a.set_dataset_for_class()
a.add_to_file()
a.read_data_json()

a.return_vacancies()
# print(a)

# print(dataset)
a.get_vacancy_from_file()
# a.return_vacancies()
print(a)
# a.remove_from_file()

# with open(path_to_data_json, 'r', encoding='utf-8') as json_file:
#     info_about_vacancies = json.load(json_file)
#
# print(info_about_vacancies)