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

class PostgresTableStrorage():

    record = []
    all_books = session.query(Books)

    def create(self, **params):
        existing_book_id = [book.book_id for book in self.all_books]

        # to ensure every book_id is unique
        if not params['book_id'] in existing_book_id:
            session.add(Books(book_id = params['book_id'], author = params['author'], title = params['title']))
            session.commit()
        return 'Book ID already exist, enter a different book!'


    def fetch(self, **params):

        # return all from database that matches the arguments provided
        for book in self.all_books:
            for value in params.values():
                if value == book.book_id or value == book.title or value == book.author:
                    self.record.append({'book_id': book.book_id, 'author': book.author, 'title': book.title})
        return self.record


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



# ///////////////////////////////////////////////////
book_manager = PostgresTableStrorage()
# book_m = book_manager.create(book_id = 101, author = 'Hal', title = 'Python')
# print(book_m)

# book_i = book_manager.fetch(book_id = 105, author = 'Ola')
# print(book_i)

book_d = book_manager.delete(book_id = 101, author = 'Tolu')
# print(book_d)
# book_manager.create(book_id=103,author = 'Tolu', title='Java')
# book_manager.create(book_id=104,author = 'Ola', title='Java')
# bookie = book_manager.create(book_id=105,author = 'Bola', title='JavaScript')
# print(bookie)


# # myBooks = book_manager.fetch(book_id = 104, author = 'Bola')
# print(myBooks)

print(book_manager.return_all())
