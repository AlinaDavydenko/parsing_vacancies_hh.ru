from src.hh_ru_parsing_data import HeadHunterAPI
from src.work_with_file import WorkWithFile
from src.work_with_vacancies import Vacancy

# vacancy = input('Введите название вакансии')
print('Осуществляется поиск вакансий')

# блок кода HeadHunterAPI
hh_vacancies = HeadHunterAPI('Moscow', 1, 1, 'Python')
hh_vacancies.get_params()
vacancies = hh_vacancies.parsing_data()
# print(vacancies)

# блок кода WorkWithFile
g_vacancies = WorkWithFile()
g_vacancies.add_to_file(vacancies)  # добавляем в файл
g_vacancies.read_data_json()  # формируем объекты для класса Vacancy

for vacancy in g_vacancies.info_about_vacancies:
    print(vacancy)


# блок кода Vacancy
# vac = Vacancy('Python', '', 20000, '')
