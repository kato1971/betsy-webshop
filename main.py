from models import *

# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line


def search(term):
    term = term.lower()
    query = (Product
             .select()
             .where(
                 Product.name.contains(term) | Product.description.contains(term)))
    
    search_result = []
    
    for product in query:      
       
        if product not in search_result:
            search_result.append(product.name)
            search_result.append(product.description)
        return search_result

# print('search for tv: ', search('tvr'))
# print('search for pc: ',search('pc')) 
# print('search for lenovo: ',search('lenovo'))
# print('search for apple: ',search('apple'))


def list_user_products(user_id):
    query = (Product.select()
             .join(User)
             .where(User.id == user_id))
    
    user_list = []

    for product in query:
        if product.name not in user_list:
            user_list.append(product.name)
    return user_list

# print('products for Kato: ', list_user_products('1'))
# print('products for Michael: ', list_user_products('2'))
# print('products for Rachel: ', list_user_products('3'))


def list_products_per_tag(tag_id):
    query = Product.select().join(ProductTag).join(Tag).where(Tag.id == tag_id)
    
    product_per_tag = []
    for products in query:
        if products not in product_per_tag:
            product_per_tag.append(products.description)
    return product_per_tag


# print(list_products_per_tag(1))
# print(list_products_per_tag(2))
# print(list_products_per_tag(5))
# print(list_products_per_tag(3))


def add_product_to_catalog(user_id, product_name, product_description, product_price, product_quantity):
    add_product = Product.create(
        name = product_name, 
        description = product_description, 
        price_per_unit = product_price, 
        quantity_in_stock = product_quantity, 
        owner = user_id
        )
    return add_product
    
# add_product_to_catalog(1, 'keyboard', 'Trust qwerty keyboard', 39.95, 25)
# print(list_user_products(1))


def remove_product(product_id):
    query = Product.delete().where(Product.id == product_id)
    return query.execute()

# remove_product(6)


def update_stock(product_id, new_quantity):
    query = Product.update(quantity_in_stock = new_quantity).where(Product.id == product_id)
    return query.execute()

# update_stock(4, 10)


def purchase_product(buyer_id, product_id, quantity):
    add_transaction = Track_transactions.create(buyer = buyer_id, purchased_product = product_id, quantity_purchased_items = quantity)
    
    query_current_stock = Product.select().where(Product.id == product_id)
    
    for amount in query_current_stock:
        current_stock = amount.quantity_in_stock
        if current_stock < quantity:
            return print(f"Out of stock")
        else:
            sum_updated_stock = current_stock - quantity
            return add_transaction, update_stock(product_id, sum_updated_stock)

# purchase_product(1, 2, 2)
# purchase_product(3, 4, 9)
