import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    print(sqlalchemy.__version__)
    engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/test_database')

    with engine.connect() as connection:
        result = connection.execute(" SELECT * FROM book")
        for row in result:
            print(row)
        result.close()
        # transaction = connection.begin()
        # try:
        #     connection.execute(
        #         "INSERT INTO book(book_id, title, isbn, publisher_id, weight) VALUES (4,'title','isbn',1,50)")
        #     transaction.commit()
        # finally:
        #     transaction.rollback()
        # with connection.begin() as transaction:
        #     connection.execute(
        #         "INSERT INTO book(book_id, title, isbn, publisher_id, weight) VALUES (5,'title','isbn',1,50)")

    print('declarative_base')
    Base = declarative_base()


    class new_author(Base):
        __tablename__ = 'new_author'
        new_author_id = Column(Integer, primary_key=True)
        full_name = Column(String(256))
        rating = Column(Float)


    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # author = new_author(new_author_id=16, full_name="Kto-to2", rating=5.7)
    # session.add(author)
    session.commit()
    for i in session.query(new_author).order_by(new_author.new_author_id):
        print(i.new_author_id, i.full_name, i.rating)
    print('------')
    for i in session.query(new_author).filter(new_author.rating > 5):
        print(i.new_author_id, i.full_name, i.rating)
