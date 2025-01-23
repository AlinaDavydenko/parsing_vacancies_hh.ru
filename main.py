from src.hh_ru_parsing_data import HeadHunterAPI
from src.work_with_file import WorkWithFile
import pandas as pd

if __name__ == "__main__":
    vacancy = input('Введите название вакансии')
    top_n_vacancy = int(input('Введите количество отображаемых вакансий'))
    print('Осуществляется поиск вакансий')

    # блок кода HeadHunterAPI
    hh_vacancies = HeadHunterAPI('Moscow', 1, 1, 'Аналитик данных')  # vacancy is __ inputted
    hh_vacancies.get_params()
    vacancies = hh_vacancies.parsing_data()
    # print(vacancies)

    # блок кода WorkWithFile, рабобта с файлом
    g_vacancies = WorkWithFile()
    g_vacancies.add_to_file(vacancies)  # добавляем в файл
    g_vacancies.read_data_json()  # формируем объекты для класса Vacancy

    is_sorting = input("Хотите отсортировать вакансии? (Y/N): ")
    if is_sorting.lower() == 'y':
        sorting_direction = input("Сортировка будет по возрастанию или убыванию? (ASC/DESC): ")
        if sorting_direction.lower() == 'desc':
            reverse = True
        else:
            reverse = False
        [print(v) for v in sorted(g_vacancies.info_about_vacancies, reverse=reverse)]
    else:
        print("Вакансии не отсортированы, но сохранены в файл!")

    # найти топ n вакансий
    is_top_n_vacancy = input(f'Вывести топ {top_n_vacancy} вакансий? (Y/N):')
    if is_top_n_vacancy.lower() == 'y':
        df = pd.DataFrame(g_vacancies.info_about_vacancies)
        print(df.head(10))
    else:
        print('Вакансии не выведены.')
