from peewee import *

db = SqliteDatabase('betsy-webshop.db')


class BaseModule(Model):
    class Meta:
        database = db


class User(BaseModule):
    name = CharField(null=False)
    street = CharField()
    zipcode = CharField()
    city = CharField()
    account_number = CharField()


class Tag(BaseModule):
    name = CharField(unique=True, max_length=50)


class Product(BaseModule):
    name = CharField()
    description = TextField()
    price_per_unit = DecimalField(
        max_digits=6,
        decimal_places=2,
        auto_round=True,
        null=False,
        default=0,
        constraints=[
            Check('price_per_unit >= 0')
        ])
    quantity_in_stock = IntegerField(
        null=False,
        default=0,
        constraints=[
            Check('quantity_in_stock >= 0')
        ])
    owner = ForeignKeyField(User, backref='products')


class Track_transactions(BaseModule):
    buyer = ForeignKeyField(User)
    purchased_product = ForeignKeyField(Product)
    quantity_purchased_items = IntegerField(
        null=False,
        constraints=[
            Check('quantity_purchased_items >= 1')
        ])

    

class ProductTag(BaseModule):
    product = ForeignKeyField(Product, backref='tags')
    tag = ForeignKeyField(Tag, backref='tags')