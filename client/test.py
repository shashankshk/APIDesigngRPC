from unittest.mock import MagicMock
from inventory_client import client
import unittest
from get_book_titles import get_book_titles
from service import protos_pb2

# Testing get_book_titles method
class TestGetBookTitlesMethod(unittest.TestCase):
    def test(self):
        thing = client('localhost','50051')
        client.getBooks = MagicMock()
        client.__init__ = MagicMock(return_value = None)
        book1 = protos_pb2.Book(ISBN="123456", title="xyz", author="a", genre='NON_FICTION', publishing_year= 1997)
        book2 = protos_pb2.Book(ISBN="234567", title="abc", author="a", genre='NON_FICTION', publishing_year= 1997)
        client.getBooks.side_effect = [book1, book2]
        result = get_book_titles(thing, ["123456", "234567"])
        client.getBooks.assert_called_with("234567")
        # Assering if result is as expected
        self.assertEqual(result, ["xyz", "abc"])
    
#  Testing actual server
class SubTest(unittest.TestCase):
    def testServer(self):
        # Starting server
        grpc_client = client('localhost','50051')
        result = grpc_client.getBooks("234567")
        # Testing title for the book
        self.assertEqual(result.title, "The Hitchhiker's Guide to the Galaxy")
        # Testing ISBN for the book
        self.assertEqual(result.ISBN, "234567")

if __name__ == '__main__':
    unittest.main()