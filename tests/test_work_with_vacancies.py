import unittest

import pytest

from src.work_with_vacancies import Vacancy


class TestVacancy(unittest.TestCase):
    """ класс тестирует Vacancy """

    def test_vacancy_init(self):
        salary = {'from': 50000, 'to': 10000}

        vacancy = Vacancy(vacancy_name="Python Developer", vacancy_link="https://example.com", salary=salary,
                          area='Remote')

        self.assertEqual(vacancy.vacancy_name, "Python Developer")
        self.assertEqual(vacancy.vacancy_link, "https://example.com")
        self.assertEqual(vacancy.area, "Remote")
        self.assertEqual(vacancy.salary_from, 50000)
        self.assertEqual(vacancy.salary_to, 10000)

    def test_vacancy_initialization_with_no_salary(self):
        """Тестирование инициализации объекта Vacancy, если зарплата не задана."""
        vacancy = Vacancy(vacancy_name="Python Developer", vacancy_link="https://example.com", salary=None,
                          area="Remote")

        self.assertEqual(vacancy.salary_from, 0)
        self.assertEqual(vacancy.salary_to, 0)

    def test_vacancy_initialization_with_missing_from_or_to_salary(self):
        """Тестирование корректной работы, если salary = NAN"""
        salary = {'from': 50000, 'to': None}
        vacancy = Vacancy(vacancy_name="Python Developer", vacancy_link="https://example.com", salary=salary,
                          area="Remote")

        self.assertEqual(vacancy.salary_from, 50000)
        self.assertEqual(vacancy.salary_to, 0)

    def test_vacancy_comparison_lt(self):
        """Тестирование магического метода __lt__ (сравнение объектов)."""
        salary1 = {'from': 50000, 'to': 100000}
        salary2 = {'from': 60000, 'to': 120000}
        vacancy1 = Vacancy(vacancy_name="Junior Developer", vacancy_link="https://example1.com", salary=salary1,
                           area="Remote")
        vacancy2 = Vacancy(vacancy_name="Senior Developer", vacancy_link="https://example2.com", salary=salary2,
                           area="Remote")

        self.assertTrue(vacancy1 < vacancy2)
        self.assertFalse(vacancy2 < vacancy1)

    def test_vacancy_comparison_lt_with_equal_salaries(self):
        """Тестирование сравнения объектов с одинаковыми значениями зарплаты."""
        salary = {'from': 50000, 'to': 100000}
        vacancy1 = Vacancy(vacancy_name="Junior Developer", vacancy_link="https://example1.com", salary=salary,
                           area="Remote")
        vacancy2 = Vacancy(vacancy_name="Junior Developer", vacancy_link="https://example2.com", salary=salary,
                           area="Remote")

        self.assertFalse(vacancy1 < vacancy2)
        self.assertFalse(vacancy2 < vacancy1)

    def test_vacancy_str_method(self):
        """Тестирование метода __str__ для корректного вывода строки."""
        salary = {'from': 50000, 'to': 100000}
        vacancy = Vacancy(vacancy_name="Python Developer", vacancy_link="https://example.com", salary=salary,
                          area="Remote")

        expected_str = "Python Developer, https://example.com, зп от 50000 до 100000"
        self.assertEqual(str(vacancy), expected_str)


if __name__ == '__main__':
    unittest.main()
