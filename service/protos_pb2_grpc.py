# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import protos_pb2 as protos__pb2


class InventoryServiceStub(object):
    """Services of inventory
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/protos.InventoryService/CreateBook',
                request_serializer=protos__pb2.Book.SerializeToString,
                response_deserializer=protos__pb2.CreateBookResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/protos.InventoryService/GetBook',
                request_serializer=protos__pb2.BookRequest.SerializeToString,
                response_deserializer=protos__pb2.Book.FromString,
                )


class InventoryServiceServicer(object):
    """Services of inventory
    """

    def CreateBook(self, request, context):
        """Service to create a book
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Service to fetch a book based on ISBN
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=protos__pb2.Book.FromString,
                    response_serializer=protos__pb2.CreateBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=protos__pb2.BookRequest.FromString,
                    response_serializer=protos__pb2.Book.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protos.InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Services of inventory
    """

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.InventoryService/CreateBook',
            protos__pb2.Book.SerializeToString,
            protos__pb2.CreateBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protos.InventoryService/GetBook',
            protos__pb2.BookRequest.SerializeToString,
            protos__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
