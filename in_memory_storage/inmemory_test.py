import unittest
from .inmemorystorage import InMemoryStorage


class InMemoryTest(unittest.TestCase):

    def setUp(self):
        return super().setup()

    def test_create(self):
        InMemoryStorage().create(author='Ade', title='Java')
        self.assertIn(self.books, {id: len(self.books), 'author': 'Ade', 'title': 'Java'})

    def test_fetch(self):
        InMemoryStorage().fetch(id=1), {id: 1, 'author': 'Ade', 'title': 'Java'}
        InMemoryStorage().fetch(author='Ade'), {id: 1, 'author': 'Ade', 'title': 'Java'}
        InMemoryStorage().fetch(title='Java'), {id: 1, 'author': 'Ade', 'title': 'Java'}

    def test_delete(self):
        InMemoryStorage().delete(id = 1)
        self.assertNotIn(self.books, {id: 1, 'author': 'Ade', 'title': 'Java'})

    def test_all(self):
        InMemoryStorage.all()
        self.assertListEqual(self.books, [{id: 1, 'author': 'Ade', 'title': 'Java'}])
