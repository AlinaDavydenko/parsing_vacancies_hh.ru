import unittest

import pytest

from src.work_with_vacancies import Vacancy


class TestVacancy(unittest.TestCase):
    """ класс тестирует Vacancy """

    def setUp(self):
        """ инициализация """
        self.vacancy_object1 = Vacancy('Python', 'https:', 5, 'Москва')
        self.vacancy_object2 = Vacancy('Developer', 'https:', 8, 'Москва')

    def test_init(self):
        """ тестирование создания экземпляров """
        self.assertEqual(self.vacancy_object1.vacancy_name, 'Python')
        self.assertEqual(self.vacancy_object1.vacancy_link, 'https:')
        self.assertEqual(self.vacancy_object1.salary, 5)
        self.assertEqual(self.vacancy_object1.area, 'Москва')

    def test_validate_salary(self):
        """ тестирование валидации зарплаты """
        salary_data = {'from': 1000, 'to': 5000}
        self.vacancy_object1._Vacancy__validate_salary(salary_data)
        self.assertEqual(self.vacancy1.salary_from, 50000)
        self.assertEqual(self.vacancy1.salary_to, 150000)

        salary_data_nan = None
        self.vacancy1._Vacancy__validate_salary(salary_data_nan)
        self.assertEqual(self.vacancy1.salary_from, 0)
        self.assertEqual(self.vacancy1.salary_to, 0)

    def test_lt_method(self):
        """ Тест магического метода сравнения """
        salary_data1 = {'from': 90000, 'to': 120000}
        salary_data2 = {'from': 70000, 'to': 100000}
        self.vacancy1._Vacancy__validate_salary(salary_data1)
        self.vacancy2._Vacancy__validate_salary(salary_data2)

        self.assertTrue(self.vacancy2 < self.vacancy1)

    def test_str_method(self):
        """ Тест метода str для красивого вывода """
        salary_data = {'from': 60000, 'to': 110000}
        self.vacancy1._Vacancy__validate_salary(salary_data)
        expected_output = 'Программист, http://example.com/job1, зп от 60000 до 110000'
        self.assertEqual(str(self.vacancy1), expected_output)

    if __name__ == '__main__':
        unittest.main()
