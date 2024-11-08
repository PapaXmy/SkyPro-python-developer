import json

from flask import request
from models import *

# users


@app.route("/users", methods=["GET", "POST"])
def users_all_page():
    if request.method == "GET":
        user_response = []

        for user in User.query.all():
            user_response.append(user.create_dict())

        return json.dumps(user_response, ensure_ascii=False)

    if request.method == "POST":
        user_data = json.loads(request.data)
        new_user = User(
            id=user_data.get("id"),
            first_name=user_data.get("first_name"),
            last_name=user_data.get("last_name"),
            age=user_data.get("age"),
            email=user_data.get("email"),
            role=user_data.get("role"),
            phone=user_data.get("phone"),
        )
        db.session.add(new_user)
        db.session.commit()
        return "Пользователь добавлен!"


@app.route("/users/<int:id>", methods=["GET", "PUT", "DELETE"])
def users_page_id(id: int):
    if request.method == "GET":
        return json.dumps(User.query.get(id).create_dict(), ensure_ascii=False)

    if User.query.get(id) is None:
        return "Пользователь не найден!"

    if request.method == "PUT":
        user_data = json.loads(request.data)
        update_user = User.query.get(id)
        update_user.first_name = user_data.get("first_name")
        update_user.last_name = user_data.get("last_name")
        update_user.age = user_data.get("age")
        update_user.email = user_data.get("email")
        update_user.role = user_data.get("role")
        update_user.phone = user_data.get("phone")

        db.session.add(update_user)
        db.session.commit()

        return "Данные пользователя обновлены!"

    if request.method == "DELETE":
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return "Пользователь удален!"


# offers


@app.route("/offers", methods=["GET", "POST"])
def offers_page():

    if request.method == "GET":
        offers_response = []

        for offer in Offer.query.all():
            offers_response.append(offer.create_dict())
        return json.dumps(offers_response, ensure_ascii=False)

    if request.method == "POST":
        user_data = json.loads(request.data)
        new_offer = Offer(
            id=user_data.get("id"),
            order_id=user_data.get("order_id"),
            executor_id=user_data.get("executor_id"),
        )
        db.session.add(new_offer)
        db.session.commit()

        return "Предложение добавлено!"


@app.route("/offers/<int:id>", methods=["GET", "PUT", "DELETE"])
def offers_id_page(id):
    if request.method == "GET":
        return json.dumps(Offer.query.get(id).create_dict())

    if Offer.query.get(id) is None:
        return "Предложение не найдено!"

    if request.method == "PUT":
        offer_data = json.loads(request.data)

        update_offer = Offer.query.get(id)
        update_offer.offer_id = offer_data.get("order_id")
        update_offer.executor_id = offer_data.get("executor_id")

        db.session.add(update_offer)
        db.session.commit()

        return "Предложение обновлено!"

    if request.method == "DELETE":
        offer = Offer.query.get(id)
        db.session.delete(offer)
        db.session.commit()

        return "Предлжение удалено!"


# orders


@app.route("/orders", methods=["GET", "POST"])
def page_orders():
    if request.method == "GET":
        order_response = []

        for order in Order.query.all():
            order_response.append(order.create_dict())
        return json.dumps(order_response, ensure_ascii=False)

    if request.method == "POST":
        order_data = json.loads(request.data)
        new_order = Order(
            id=order_data.get("id"),
            name=order_data.get("name"),
            description=order_data.get("description"),
            start_date=order_data.get("start_date"),
            end_date=order_data.get("end_date"),
            adress=order_data.get("adress"),
            price=order_data.get("price"),
            customer_id=order_data.get("customer_id"),
            executor_id=order_data.get("customer_id"),
        )
        db.session.add(new_order)
        db.session.commit()

        return "Заказ добавлен!"


@app.route("/orders/<int:id>", methods=["GET", "PUT", "DELETE"])
def order_id_page(id):
    if request.method == "GET":
        return json.dumps(Order.query.get(id).create_dict(), ensure_ascii=False)

    if Order.query.get(id) is None:
        return "Заказ не найден!"

    if request.method == "PUT":
        order_data = json.loads(request.data)
        update_order = Order.query.get(id)
        update_order.name = order_data.get("name")
        update_order.description = order_data.get("description")
        update_order.start_date = order_data.get("start_date")
        update_order.end_date = order_data.get("end_date")
        update_order.adress = order_data.get("adress")
        update_order.price = order_data.get("price")
        update_order.customer_id = order_data.get("customer_id")
        update_order.executor_id = order_data.get("customer_id")

        db.session.add(update_order)
        db.session.commit()

        return "Заказ обновлен!"

    if request.method == "DELETE":
        order = Order.query.get(id)
        db.session.delete(order)
        db.session.commit()

        return "Заказ удален!"
