import models
import os

def main():
    populate_test_database()


def populate_test_database():
    models.db.connect()
    models.db.create_tables([models.User, models.Product, models.Tag, models.Track_transactions, models.ProductTag])

    users = [
        ('Kato', 'Street 1', '1234 AA', 'City1', '12345678'),
        ('Michael', 'Street 2', '1234 BB', 'City2', '87654321'),
        ('Rachel', 'Street 3', '1234 CC', 'City3', '12348765'),
        ]
    products = [
        ('tv', 'LG TV 43 inch', '369.50', '10', '3'),
        ('pc', 'Lenovo PC 27 inch', '1599.00', '5', '1'),
        ('tablet', 'Samsung Tablet 10 inch', '250.99', '15', '2'),
        ('tv', 'Samsung TV 40 inch', '499.00', '5', '2'),
        ('mac', 'Aplle Mac PC 40 inch', '1345.00', '3', '3'),
    ]
    tags = [
        ('tv'), 
        ('pc'), 
        ('tablet'),
        ('samsung'),
        ('lenovo'),
        ('apple'),
        ('lg'),
    ]
    transactions = [
        (1, 3, 1), 
        (2, 1, 1), 
        (3, 2, 1),
    ]
    product_tags = [
        (1, 1),
        (1, 7),
        (2, 2),
        (2, 5),
        (3, 3),
        (3, 4),
        (4, 1),
        (4, 4),
        (5, 2),
        (5, 6)
    ]

    for user in users:
        models.User.create(
            name=user[0],
            street=user[1],
            zipcode=user[2], 
            city=user[3],
            account_number=user[4],
        )

    for product in products:
        models.Product.create(
            name=product[0], 
            description=product[1], 
            price_per_unit=product[2], 
            quantity_in_stock=product[3], 
            owner=product[4]
        )
        
    for name in tags:
        models.Tag.create(
            name=name
        )

    for transaction in transactions:
        models.Track_transactions.create(
            buyer=transaction[0], 
            purchased_product=transaction[1], 
            quantity_purchased_items=transaction[2],
        )

    for producttag in product_tags:
        models.ProductTag.create(
            product=producttag[0], 
            tag=producttag[1],
        )

def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "betsy-webshop.db")
    if os.path.exists(database_path):
        os.remove(database_path)



if __name__== 'main':
    main()