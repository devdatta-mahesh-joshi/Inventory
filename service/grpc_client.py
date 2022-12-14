import logging
from concurrent import futures

import grpc
import library_pb2
import library_pb2_grpc
import services_pb2
import services_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = services_pb2_grpc.InventoryServiceStub(channel)
        
        print("CREATING A BOOK NOW")
        book = library_pb2.Book()
        book.ISBN = "99"
        book.title = "Book99"
        book.author = "Author99"
        book.genre = 2
        book.publishingYear.year=1999
        response = stub.CreateBook(services_pb2.CreateBookRequest(book=book))
        print(response)

        print("FETCHING A BOOK BY ISBN NOW")
        response = stub.GetBook(services_pb2.GetBookRequest(book="99"))
        print(response)
        
        
    


if __name__ == '__main__':
    logging.basicConfig()
    run()