from model import Base, Dog, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_Product(name, price, picture_link, description):

    Dog_object = Dog(
        name=name,
        price=price,
        picture_link=picture_link,
        description=description)

    session.add(Dog_object)
    session.commit()


add_Product("book", 60, "https://cdn.shopify.com/s/files/1/0882/3478/articles/Book_Log_1400x.progressive.jpg?v=1549548939", "this is a cool book")

def delete_product(name):
	session.query(Dog).filter_by(
		name=name).first().delete()
	session.commit()


def update_product(name, price, picture_link, description):

	Dog1 = session.query(Dog).filter_by(
		name=name).first()
	Dog1.name = name
	Dog1.picture_link = picture__link
	Dog1.description = description

	session.commit()

def query_by_id(id):
	Dog1 = session.query(Dog).filter_by(id=id).first()
	return Dog1

def query_all():
	Dog1 = session.query(Dog).all()
	return Dog1

	
def add_to_cart(ProductID):

	Cart_object=Cart(
		ProductID=ProductID)
	session.add(Cart_object)
	session.commit()


# add_Product("Max", "Priceless", "dog3.jpg", "Cute dog. A bit of a cry baby. pls adopt... ASAP!")
# products = query_all()










   


# print(query_by_name("Mayuri"))
