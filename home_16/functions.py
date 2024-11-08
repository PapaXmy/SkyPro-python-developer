import json


def load_users():
    with open("./data/users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_offers():
    with open("./data/offers.json", "r", encoding="utf-8") as file:
        return json.load(file)


def load_orders():
    with open("./data/orders.json", "r", encoding="utf-8") as file:
        return json.load(file)


# print(load_users())
# print(load_offers())
# print(load_orders())
