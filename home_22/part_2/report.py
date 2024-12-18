# Я изучил работу https://github.com/VladimirShtefan/Lesson_21_Abstract_methods
# Я обнаружил следующие запахи:

# - файл transaction.py, строки 15-21
# - сложность создания словаря store_dict
# - как бы я переписал:

def start_transaction(self, store_dict: dict[str, BaseStorage]) - None:
    sender = store_dict[self._from_store]
    receiver = store_dict[self._to_store]


# - файл transaction.py, строки 27-31
# - формирование сообщений внутри метода start_transaction, можно
# выделить в отдельный метод
# - как бы я переписал:

def _log_transaction(self, sender: BaseStorage, receiver: BaseStorage) -> None:
    print(f"Курьер забрал {self._amount} {self._product} из {sender.get_storage()}")
    print(f"Курьер доставил {self._amount} {self._product} в {receiver.get_storage()}")


# - файл transaction.py, строки 38-43
# - повторение кода вывода информации о состоянии магазина, можно
# так же выделить в отдельный метод
# - как бы я переписал:

def _log_storage_status(self, sender: BaseStorage, receiver: BaseStorage) -> None:
    print(f'{sender.get_storage_name()} хранит: {sender.get_items()}')
    print(f"{receiver.get_storage_name()} хранит: {receiver.get_items()}")

# - файл transaction.py, строки 14-43
# - слишком длинный метод start_transaction
# - как бы я переписал с учетом найденых запахов:

class Transaction:
    def __init__(self, from_store: str, to_store: str, amount: int, product: str):
        self._from_store = from_store
        self._to_store = to_store
        self._amount = amount
        self._product = product

    def start_transaction(self, store_dict: dict[str, BaseStorage]) -> None:
        sender = store_dict[self._from_store]
        receiver = store_dict[self._to_store]
        self._process_transaction(sender, receiver)

    def _process_transaction(self, sender: BaseStorage, receiver: BaseStorage):
        try:
            self._remove_transaction(sender)
            self._add_transaction(receiver)
            self._log_transaction(sender, receiver)
        except BaseError as e:
            print(e.message)
            self._add_transaction(sender)
        finally:
            self._log_storage_status(sender, receiver)

    
    def _log_transaction(self, sender: BaseStorage, receiver: BaseStorage) -> None:
        print(f"Курьер забрал {self._amount} {self._product} из {sender.get_storage()}")
        print(f"Курьер доставил {self._amount} {self._product} в {receiver.get_storage()}")


    def _log_storage_status(self, sender: BaseStorage, receiver: BaseStorage) -> None:
        print(f'{sender.get_storage_name()} хранит: {sender.get_items()}')
        print(f"{receiver.get_storage_name()} хранит: {receiver.get_items()}")


    def _remove_transaction(self, sender: BaseStorage) -> None:
        sender.remove(amount=self._amount, name=self._product)

    def _add_transaction(self, receiver: BaseStorage):
        receiver.add(amount=self._amount, name=self._product)
