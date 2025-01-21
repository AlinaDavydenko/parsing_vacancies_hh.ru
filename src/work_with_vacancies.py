
from pandas import DataFrame


class Vacancy:
    """ класс для работы с вакансиями """
    dataset: dict
    df_categories: DataFrame

    def __init__(self, vacancy_name: str, vacancy_link: str, salary: int, area: str):
        """ инициализация элементов проверки """
        self.vacancy_name = vacancy_name
        self.vacancy_link = vacancy_link
        self.area = area
        self.__validate_salary(salary)

    def __validate_salary(self, salary):
        """ валидация по зарплате """
        if salary:
            self.salary_from = salary['from'] if salary['from'] else 0
            self.salary_to = salary['to'] if salary['to'] else 0
        else:
            self.salary_from = 0
            self.salary_to = 0

    def __lt__(self, other):
        """ магический метод сравнения """
        return self.salary_from < other.salary_from

    def __str__(self):
        """ красивый вывод """
        return f'{self.vacancy_name}, {self.vacancy_link}, зп от {self.salary_from} до {self.salary_to}'
