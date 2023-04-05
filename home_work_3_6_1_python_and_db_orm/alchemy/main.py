import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:Qwerty@localhost:5432/netology'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

# session.add(Publisher(name='Пушкин'))
# session.add(Publisher(name='Лермонтов'))
# session.add(Publisher(name='Гоголь'))
# session.add(Shop(name="Буквоед"))
# session.add(Shop(name="Лабиринт"))
# session.add(Shop(name="Книжный дом"))
# session.add(Book(title="Капитанская дочка", id_publisher=1))
# session.add(Book(title="Евгений Онегин", id_publisher=1))
# session.add(Book(title="Руслан и Людмила", id_publisher=1))
# session.add(Stock(id_book=1, id_shop=1, count=1))
# session.add(Stock(id_book=3, id_shop=1, count=1))
# session.add(Stock(id_book=1, id_shop=2, count=1))
# session.add(Stock(id_book=2, id_shop=3, count=1))
# session.add(Stock(id_book=1, id_shop=1, count=1))
# session.add(Sale(price=600, date_sale='9-11-2022', id_stock=1, count=1))
# session.add(Sale(price=500, date_sale='8-11-2022', id_stock=2, count=1))
# session.add(Sale(price=580, date_sale='5-11-2022', id_stock=3, count=1))
# session.add(Sale(price=490, date_sale='2-11-2022', id_stock=4, count=1))
# session.add(Sale(price=600, date_sale='26-10-2022', id_stock=5, count=1))

publisher_name = input('Введите фамилию автора: ')

shops = session.query(Shop)\
    .join(Stock, Shop.id == Stock.id_shop)\
    .join(Book, Stock.id_book == Book.id)\
    .join(Publisher, Book.id_publisher == Publisher.id)\
    .filter(Publisher.name == publisher_name)\
    .distinct()

for shop in shops:
    sales = session.query(Sale)\
        .join(Stock, Sale.id_stock == Stock.id)\
        .join(Book, Stock.id_book == Book.id)\
        .join(Publisher, Book.id_publisher == Publisher.id)\
        .filter(Publisher.name == publisher_name)\
        .filter(Stock.id_shop == shop.id)

    for sale in sales:
        print(f"{sale.stock.book.title} | {shop.name} | {sale.price} | {sale.date_sale.strftime('%d-%m-%Y')}")

session.commit()

session.close()