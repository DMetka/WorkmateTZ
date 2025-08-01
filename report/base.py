from abc import ABC, abstractmethod


class BaseReport(ABC):
    def __init__(self, entries):
        self.entries = entries

    @abstractmethod
    def generate(self):
        pass
