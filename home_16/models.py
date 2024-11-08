from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from functions import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///homework_base.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(20))
    phone = db.Column(db.String(20))

    def create_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone,
        }


class Offer(db.Model):
    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def create_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }


#    order = db.relationship("Order")
#    executor = db.relationship("User")


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))
    adress = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def create_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "adress": self.adress,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id,
        }


#    customer = db.relationship("User")
#    executor = db.relationship("User")


with app.app_context():
    db.drop_all()
    db.create_all()

    for user in load_users():
        new_user = User(
            id=user.get("id"),
            first_name=user.get("first_name"),
            last_name=user.get("last_name"),
            age=user.get("age"),
            email=user.get("email"),
            role=user.get("role"),
            phone=user.get("phone"),
        )

        db.session.add(new_user)
        db.session.commit()

    for offer in load_offers():
        new_offer = Offer(
            id=offer.get("id"),
            order_id=offer.get("order_id"),
            executor_id=offer.get("executor_id"),
        )

        db.session.add(new_offer)
        db.session.commit()

    for order in load_orders():
        new_order = Order(
            id=order.get("id"),
            name=order.get("name"),
            description=order.get("description"),
            start_date=order.get("start_date"),
            end_date=order.get("end_date"),
            adress=order.get("adress"),
            price=order.get("price"),
            customer_id=order.get("customer_id"),
            executor_id=order.get("executor_id"),
        )

        db.session.add(new_order)
        db.session.commit()
