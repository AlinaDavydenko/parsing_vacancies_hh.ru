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
