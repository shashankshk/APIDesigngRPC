from inventory_client import client

# Impleenting method which uses client object
def get_book_titles (client, isbnList):
    result = []
    for isbn in isbnList: 
        book = client.getBooks(isbn)
        if(not book is None):
            result.append(book.title)
    return result

# Implementing main segment
if __name__ == '__main__':
    grpc_client = client('localhost','50051')
    get_book_titles(grpc_client, ["123456", "234567"])
