from storage import Storage
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2://postgres:curly@localhost/postgres')
base = declarative_base()
Session = sessionmaker(engine)
session = Session()


class Books(base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    author = Column(String)
    title = Column(String)

class PostgresTableStrorage(Storage):

    
    all_books = session.query(Books)

    def create(self, **params):
        existing_book_id = [book.book_id for book in self.all_books]

        # to ensure every book_id is unique
        if not params['book_id'] in existing_book_id:
            session.add(Books(book_id = params['book_id'], author = params['author'], title = params['title']))
            session.commit()
        return 'Book ID already exist, enter a different book!'


    def fetch(self, **params):
        record = []
        # return all from database that matches the arguments provided
        for book in self.all_books:
            for value in params.values():
                if value == book.book_id or value == book.title or value == book.author:
                    if book not in record:

                        record.append({'book_id': book.book_id, 'author': book.author, 'title': book.title})     
        # print(record)       
        return record



    def delete(self,**params):
        # deletes all that matches the argument
        for book in self.all_books:
            for value in params.values():
                if value == book.book_id or value == book.title or value == book.author:
                    session.delete(book)
                    session.commit()
        return "Books successfully delete!"


    def return_all(self):

        allBooks = [{'book_id': book.book_id, 'author': book.author, 'title': book.title} for book in self.all_books]
        return allBooks


