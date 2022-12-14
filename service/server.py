import grpc
from concurrent import futures
from db import books,Book, Genre
import protos_pb2_grpc as pb2_grpc
import  protos_pb2 as pb2

# Creating server for inventory service
class InventoryServiceServicer(pb2_grpc.InventoryServiceServicer):
    def __init__(self):
        print("Starting server on port 50051!")
        

    # Method to fetch book from database
    def GetBook(self, request, context):
        # If ISBN is not present or is None
        if (not request.ISBNTOFIND or request.ISBNTOFIND is None):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Missing argument ISBNTOFIND')
            return pb2.Book()

        # If given ISBN does not exist
        if not request.ISBNTOFIND in books:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Book not found for given ISBN')

        # Returning data
        result = books[request.ISBNTOFIND]
        result = {'ISBN': result.ISBN, 'title': result.title, 'author': result.author, 'genre': 2, 'publishing_year': result.publishing_year}
        return pb2.Book(**result)

    # Method to create book in database
    def CreateBook(self, request, context):
        # Checking if request is valid
        if not isValidCreateBookRequest(request):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Incorrect details for creating book')
            return pb2.CreateBookResponse()
        # Creating Book object to store
        book = Book(request.ISBN, request.title, request.author, request.genre, request.publishing_year)
        books[request.ISBN] = book
        result = {"message": "Book created"}
        return pb2.CreateBookResponse(**result)

# Method to check valid book type for storing
def isValidCreateBookRequest(bookDetail):
    if  (not bookDetail.ISBN or not bookDetail.title or not bookDetail.author or not bookDetail.genre or not bookDetail.publishing_year):
        return False
    else:
        return True

# Starting server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server up and running :)")
    server.wait_for_termination()
    


if __name__ == '__main__':
    serve()