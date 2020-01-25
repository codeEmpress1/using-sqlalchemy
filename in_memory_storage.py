from .storage import Storage


class InMemoryStorage(Storage):

    def __init__(self):
        self.books = []

    def create(self, **params):
        self.books.append(params)
        return params

    def fetch(self, **params):
        my_book = [(key, value) for key, value in params.items()]
        (key, value) = my_book[0]
        for book in self.books:
            if book[key] == value:
                return book

    def delete(self, **params):
        my_book = [(key, value) for key, value in params.items()]
        (key, value) = my_book[0]
        self.books = [books for books in self.books if books[key] != value]
        return self.books

    def return_all(self):
        return self.books


# dat = InMemoryStorage()
# dat.create(book_id=1, title='Java', author='Tolu')
# dat.create(book_id=2, title="Python", author='Abdulfatai')
# dat.create(book_id=3, title='Snake', author='Tega')
# print(dat.fetch(author= 'Tolu'))
# print(dat.return_all())
