from base_class import Storage


class Store(Storage):

    def __init__(self) -> None:
        super().__init__(capacity=100)

    def add(self, name: str, quantity: int):

        if self.capacity >= quantity:

            if name in self.items:
                self.items[name] += quantity
            else:
                self.items[name] = quantity
            self.capacity -= quantity

    def remove(self, name: str, quantity: int):

        if name in self.items and self.items[name] >= quantity:
            self.items[name] -= quantity

            if self.items[name] == 0:
                del self.items[name]


class Shop(Storage):

    def __init__(self):
        super().__init__(capacity=20)

    def add(self, name: str, quantity: int):

        if self.capacity >= quantity and self.get_unique_items_count() < 5:

            if name in self.items:
                self.items[name] += quantity
            else:
                self.items[name] = quantity
            self.capacity -= quantity

    def remove(self, name: str, quantity: int):

        if name in self.items and self.items[name] >= quantity:
            self.items[name] -= quantity

            if self.items[name] == 0:
                del self.items[name]


class Request:

    def __init__(self, request_str: str) -> None:
        self.from_: str = ""
        self.to: str = ""
        self.amount: int = 0
        self.product: str = ""

        self._parse_request(request_str)

    def _parse_request(self, request_str: str):
        parts = request_str.split()

        if "забирает" in parts:
            self.amount = int(parts[2])
            self.product = parts[3]

        elif "доставить" in parts:
            self.amount = int(parts[1])
            self.product = parts[2]

        else:
            print("Некоректный запрос.")

        if "из" in parts:
            from_idx = parts.index("из") + 1
            self.from_ = parts[from_idx]
        else:
            print("Не указано место откуда забрать товар.")

        if "в" in parts:
            to_idx = parts.index("в") + 1
            self.to = parts[to_idx]
        else:
            self.to = "магазин"

    def __repr__(self):
        return (
            f"Доставить {self.amount} {self.product} "
            f"из {self.from_} в {self.to}"
        )
