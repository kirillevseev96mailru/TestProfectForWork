from abc import ABC, abstractmethod


class Report(ABC):
    """
    Базовый класс для отчётов.
    Принимает на вход список записей-словарей и
    требует реализации метода generate(), возвращающего
    список строк (rows) для табличного вывода.
    """
    def __init__(self, entries):
        self.entries = entries

    @abstractmethod
    def generate(self):
        ...
