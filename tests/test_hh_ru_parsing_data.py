# import requests

import unittest

from unittest.mock import Mock, patch

from src.hh_ru_parsing_data import HeadHunterAPI

# тестируем класс HeadHunterAPI

hh_vacancies = HeadHunterAPI('Moscow', 1, 1, 'Developer')
hh_vacancies.get_params()
data_set_vacancy = hh_vacancies.parsing_data()


class TestHeadHunterAPI(unittest.TestCase):
    """ класс тестирования HeadHunterAPI """

    @patch('requests.get')
    def test_parsing_data_good(self, mock_get):
        # экземпляр класса HeadHunterAPI
        api = HeadHunterAPI('Moscow', 1, 0, 'Developer')

        # мокаем параметры
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': ['smth from hh.ru']}
        mock_get.return_value = mock_response

        # вывод ответа
        result = api.parsing_data()

        # проверяем, когда код 200, и всё хорошо
        self.assertEqual(result, {'items': ['smth from hh.ru']})
        mock_get.assert_called_once_with(url=api.get_url(), params=api.params)

    @patch('requests.get')
    def test_parsing_data_bad(self, mock_get):
        # экземпляр класса HeadHunterAPI
        api = HeadHunterAPI('Moscow', 1, 0, 'Developer')

        # мокаем параметры
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # вывод ответа
        result = api.parsing_data()

        # проверка
        self.assertEqual(result, 'Ошибка 404')
        mock_get.assert_called_once_with(url=api.get_url(), params=api.params)

    # тетирование инициализации с помощью assert
    def setUp(self):
        """ Метод для настройки тестов, выполняется перед каждым тестом. """
        self.example_class = HeadHunterAPI('Moscow', 1, 0, 'Developer')

    def test_initialize(self):
        assert self.example_class.city == 'Moscow'
        assert self.example_class.number_of_city == 1

    def get_params_data(self):
        params = {
            'text': f"{self.example_class.vacancy} {self.example_class.city}",
            'area': 1,
            'specialization': {self.example_class.number_of_city},
            'per_page': 100,
            'page': self.example_class.page
        }
        return params

    def test_get_params(self):
        data_for_test = self.get_params_data()
        self.assertEqual(self.example_class.get_params(), data_for_test)


if __name__ == '__main__':
    unittest.main()
