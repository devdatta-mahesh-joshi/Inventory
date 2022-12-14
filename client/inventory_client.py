import logging
import sys
from concurrent import futures

import grpc

sys.path.append('../service/')

import data
import library_pb2
import library_pb2_grpc
import services_pb2
import services_pb2_grpc


class inventory_client:

    def CreateBookFromData(self, b):
        # The function takes a book entry as input and returns a gRPC Book object
        book = library_pb2.Book()
        book.ISBN = b["ISBN"]
        book.title = b["title"]
        book.author = b["author"]
        book.genre = b["genre"]
        book.publishingYear.year= b["publishingYear"]
        return book

    def __init__(self, ip, port) -> None:
        # To connect client to the server
        self.server = ip + ":" + port
        pass

    def CreateBook(self, book):
        # This function takes a book entry as input and sends a gRPC request to create this book
        # Creating book object from database entry
        bookrequest = self.CreateBookFromData(book)
        with grpc.insecure_channel(self.server) as channel:
            # initializing server stub
            stub = services_pb2_grpc.InventoryServiceStub(channel)
            # sending CreateBook request to server
            response = stub.CreateBook(services_pb2.CreateBookRequest(book=bookrequest))
            return response
        return "ERROR, SERVER DOWN"

    def GetBook(self, ISBN):
        # This function takes an ISBN as input and sends a gRPC request to retrieve book with said ISBN
        with grpc.insecure_channel(self.server) as channel:
            # initializing server stub
            stub = services_pb2_grpc.InventoryServiceStub(channel)
            # sending GetBook request to server
            response = stub.GetBook(services_pb2.GetBookRequest(book=ISBN))
            return response
        return "ERROR, SERVER DOWN"


if __name__ == "__main__":
    # Main class to create object of above class and verify working
    print("FILE IS EXECUTING")
    inventory_object = inventory_client(ip="localhost", port="50051")
    print(data.books[0])
    print(inventory_object.CreateBook(book=data.books[0]))
    print(inventory_object.GetBook(ISBN="2"))
