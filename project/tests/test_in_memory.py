import unittest
# import sys
# print(sys.path)
from lib.in_memory_storage import InMemoryStorage


class TestInMemory(unittest.TestCase):
    book = InMemoryStorage()

    def setup(self):
        self.book.create(book_id=2, author='Abdulfatai', title='Python')
        self.book.create(book_id=1, author='Ade', title='Java')
        return self.book

    def tearDown(self):
        InMemoryStorage().delete(book_id=1)
        InMemoryStorage().delete(book_id=2)
        # InMemoryStorage().delete(book_id=3)

    def test_create(self):
        self.assertEqual(InMemoryStorage().create(book_id=1, author='Ade', title='Java'), {'book_id': 1, 'author': 'Ade', 'title': 'Java'})

    def test_fetch(self):
        self.book.create(book_id=2, author='Abdulfatai', title='Python')
        self.book.create(book_id=1, author='Ade', title='Java')

        self.assertDictEqual(self.book.fetch(book_id=1), {'book_id': 1, 'author': 'Ade', 'title': 'Java'})
        self.assertDictEqual(self.book.fetch(author='Abdulfatai'), {'book_id': 2, 'author': 'Abdulfatai', 'title': 'Python'})
        self.assertDictEqual(self.book.fetch(title='Java'), {'book_id': 1, 'author': 'Ade', 'title': 'Java'})

    def test_delete(self):
        self.book.create(book_id=2, author='Abdulfatai', title='Python')
        self.book.create(book_id=1, author='Ade', title='Java')


        self.book.delete(book_id=1)
        self.assertNotIn({'book_id': 1, 'author': 'Ade', 'title': 'Java'}, InMemoryStorage().books)

    def test_all(self):
        self.book.create(book_id=2, author='Abdulfatai', title='Python')
        self.book.create(book_id=1, author='Ade', title='Java')


        self.assertListEqual(self.book.return_all(), ([{'book_id': 2, 'author': 'Abdulfatai', 'title': 'Python'}, {'book_id': 1, 'author': 'Ade', 'title': 'Java'}]))


if __name__ == '__main__':
    unittest.main()
