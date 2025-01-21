import pandas as pd


def show_vacancies(df: pd.DataFrame):
    """ выводит все вакансии """
    df1 = df[['name', 'apply_alternate_url', 'address', 'area', 'salary']]

    normalize_salary = pd.json_normalize(df1['salary'])
    normalize_address = pd.json_normalize(df1['address'])

    df = pd.concat(
        [df1['name'], df1['apply_alternate_url'], normalize_salary['from'], normalize_salary['to'],
         normalize_address['city'], normalize_address['metro.station_name']],
        sort=False, axis=1)
    return df


# df = pd.DataFrame(dataset['items'])
# def get_top_n_vacancy(df: pd.DataFrame, top_n_vacancy = 5):
#     """ выводит топ N вакансий """
#     sorted_by_salary = df.sort_values(by='from')
#     top_n_vacancies = sorted_by_salary.head(top_n_vacancy)
#     return top_n_vacancies
#
#
#
#
# def salary_search(self):
#     """ выбор по зарплате, от какой зп смотреть, и сортировка от меньшего к большему """
#     cleaned_df = Vacancies.df_categories.dropna(subset=['from'])  # чистим данные от Nan
#     # сортируем данные
#     filtered_df = cleaned_df[cleaned_df['from'] >= self.salary]
#     sorted_salary = filtered_df.sort_values(by='from')
#     return f'Вакансии, которые удалось найти \n{sorted_salary}'
#
#
# def search_vacancy_for_link(self):
#     """ поиск вакансии по ссылки или имени """
#     vac = Vacancies.df_categories
#     if vac[vac['apply_alternate_url'] == self.vacancy_link] or vac[vac['name'] == self.vacancy_name]:
#         filter_df_link = vac
#         return filter_df_link
#
#
# def search_vacancy_for_metro(self):
#     """ поиск вакансий по названию метро """
#     filter_df_metro = Vacancies.df_categories[Vacancies.df_categories['metro.station_name'] == self.metro]
#     return filter_df_metro
