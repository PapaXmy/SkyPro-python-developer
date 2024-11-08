from abc import ABC, abstractmethod
from typing import Dict, Union


class Storage(ABC):

    def __init__(self, capacity):
        self.items: Dict[str, int] = {}
        self.capacity: int = capacity

    @abstractmethod
    def add(self, name: str, quantity: int) -> Union[str, None]:
        pass

    @abstractmethod
    def remove(self, name: str, quantity: int) -> Union[str, None]:
        """Удаление выбранного товара со склада"""
        pass

    def get_free_space(self) -> int:
        """Возвращает количество свободных мест на складе"""
        return self.capacity 

    def get_items(self) -> Dict[str, int]:
        """Возвращает содержание склада в словаре"""
        return self.items

    def get_unique_items_count(self) -> int:
        """Возвращает количество уникальных товаров на складе"""
        return len(self.items)
