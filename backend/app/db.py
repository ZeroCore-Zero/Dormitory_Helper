from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class User(Base):
    __tablename__ = "User"

    username = db.Column(db.String(32))
    password = db.Column(db.String(128))
    email = db.Column(db.String(64))
    name = db.Column(db.String(64))
    BUPTID = db.Column(db.String(16))


class Bill(Base):
    __tablename__ = "Bill"

    content = db.Column(db.String(32))
    payer = db.Column(db.String(32))
    price = db.Column(db.Float)
