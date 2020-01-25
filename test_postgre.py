import unittest
from postgres_table_storage import PostgresTableStrorage

class TestPostgre(unittest.TestCase):

    # this is assumed to test for create method
    def setUp(self):
        self.book = PostgresTableStrorage()

        self.book.create(book_id=101, author='Abdulfatai', title='Python')
        self.book.create(book_id=102, author='Ade', title='Java')
        self.book.create(book_id=103, author='John', title='React')
        return self.book

    # this is assumed to test for delete method
    def tearDown(self):
            PostgresTableStrorage().delete(book_id = 101, author = 'Ade')
            PostgresTableStrorage().delete(title = 'React')

    def test_fetch(self):
        result1 = PostgresTableStrorage().fetch(title = 'Java')
        self.assertListEqual(PostgresTableStrorage().fetch(book_id = 101, author = 'John')
        , [{'book_id': 101, 'author': 'Abdulfatai', 'title': 'Python'}, {'book_id': 103, 'author': 'John', 'title': 'React'}])
        
        self.assertListEqual(result1, [{'author': 'Ade', 'book_id': 102, 'title': 'Java'}])

    def test_all(self):
        self.assertIn({'book_id': 101, 'author': 'Abdulfatai', 'title': 'Python'}, PostgresTableStrorage().return_all())
        self.assertIn({'book_id': 102, 'author': 'Ade', 'title': 'Java'}, PostgresTableStrorage().return_all())
        self.assertIn({'book_id': 103, 'author': 'John', 'title': 'React'}, PostgresTableStrorage().return_all())



