import pandas as pd
import json
from pandas import DataFrame
pd.set_option('display.max_columns', None)


# TODO: методы сравнения по зарплате
#  Проверить, указана ли зп или нет
#  Валидация данных
#  найти вакансию с самой большой зарплатой и маленькой, показать вакансии в каком - то диапазоне
#  найти вакансии по ссылке и имени, расписанию и метро
#  добавить отфильтрованные вакансии в файл
#  сбросить настройки


class Vacancies:
    """ класс для работы с вакансиями """
    dataset: dict
    df_categories: DataFrame

    def __init__(self, dataset, top_n_vacancy: int, vacancy_name: str, vacancy_link: str, salary: int, metro: str):
        """ инициализация элементов проверки """
        self.dataset = dataset
        self.vacancy_name = vacancy_name
        self.vacancy_link = vacancy_link
        self.salary = salary
        self.metro = metro
        self.top_n_vacancy = top_n_vacancy

    def dataset_setter(self):
        Vacancies.dataset = self.dataset

    @classmethod
    def show_vacancies(cls):
        """ выводит все вакансии """
        df = pd.DataFrame(cls.dataset['items'])
        df1 = df[['name', 'apply_alternate_url', 'address', 'area', 'salary']]

        normalize_salary = pd.json_normalize(df1['salary'])
        normalize_address = pd.json_normalize(df1['address'])

        cls.df_categories = pd.concat(
            [df1['name'], df1['apply_alternate_url'], normalize_salary['from'], normalize_salary['to'],
             normalize_address['city'], normalize_address['metro.station_name']],
            sort=False, axis=1)
        return cls.df_categories

    def top_n_vacancy(self):
        """ выводит топ N вакансий """
        top_n_vacancies = Vacancies.df_categories.head(self.top_n_vacancy)
        return top_n_vacancies

    def salary_search(self):
        """ выбор по зарплате, от какой зп смотреть, и сортировка от меньшего к большему """
        cleaned_df = Vacancies.df_categories.dropna(subset=['from'])  # чистим данные от Nan
        # сортируем данные
        filtered_df = cleaned_df[cleaned_df['from'] >= self.salary]
        sorted_salary = filtered_df.sort_values(by='from')
        return f'Вакансии, которые удалось найти \n{sorted_salary}'

    def search_vacancy_for_link(self):
        """ поиск вакансии по ссылки или имени """
        vac = Vacancies.df_categories
        if vac[vac['apply_alternate_url'] == self.vacancy_link] or vac[vac['name'] == self.vacancy_name]:
            filter_df_link = vac
            return filter_df_link

    def search_vacancy_for_metro(self):
        """ поиск вакансий по названию метро """
        filter_df_metro = Vacancies.df_categories[Vacancies.df_categories['metro.station_name'] == self.metro]
        return filter_df_metro


# Датасет = получение данных из файла и записывание данных в новый файл
with open('../data/data.json', 'r', encoding='utf-8') as json_file:
    datasets = json.load(json_file)

mydata = Vacancies(datasets,
                   10,
                   'Директор по продажам',
                   'https://hh.ru/applicant/vacancy_response?vacancyId=115274317',
                   500000,
                   'Бауманская')
mydata.dataset_setter()
mydata.show_vacancies()

# print(Vacancies.dataset)
# print(Vacancies.df_categories)
mydata.salary_search()
print()
