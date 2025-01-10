from abc import ABC, abstractmethod


class ParsingData(ABC):
    """ абстракный класс для класса HeadHunterAPI """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

    @abstractmethod
    def parsing_data(self):
        pass


class ABCWorkWithFile(ABC):
    """ абстрактный класс для класса WorkWithFile"""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def set_dataset_for_class(self):
        pass

    @abstractmethod
    def get_vacancy_from_file(self):
        pass
