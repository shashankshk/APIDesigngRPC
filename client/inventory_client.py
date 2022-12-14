from pathlib import Path
import sys

# Adding service and proto to module path
path_root = Path(__file__).parents[1]
path_root.joinpath('proto')
sys.path.append(str(path_root.joinpath('proto')))
sys.path.append(str(path_root.joinpath('service')))
sys.path.append(str(path_root))

from service import protos_pb2_grpc
from service import protos_pb2
import grpc

# Defining client class
class client:
    def __init__(self, address, port):
        # Defining port
        self.port = port
        # Defining address
        self.address = address
        # Starting channel
        self.channel = grpc.insecure_channel(self.address +':'+ self.port)
        # Passing channel to stub
        self.stub = protos_pb2_grpc.InventoryServiceStub(self.channel)

    # Implementing method to fetch books from grpc server
    def getBooks(self, isbn):
        try:
            request = protos_pb2.BookRequest(ISBNTOFIND=isbn)
            # Fetching book using stub
            result = self.stub.GetBook(request)
        # Handling error
        except grpc.RpcError as rpc_error:    
            print(f"Fetch book error: code={rpc_error.code()} message={rpc_error.details()}: {isbn}")
        else: 
            return result

        