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
        book = library_pb2.Book()
        book.ISBN = b["ISBN"]
        book.title = b["title"]
        book.author = b["author"]
        book.genre = b["genre"]
        book.publishingYear.year= b["publishingYear"]
        return book

    def __init__(self, ip, port) -> None:
        self.server = ip + ":" + port
        pass

    def CreateBook(self, book):
        bookrequest = self.CreateBookFromData(book)
        with grpc.insecure_channel(self.server) as channel:
            stub = services_pb2_grpc.InventoryServiceStub(channel)
            response = stub.CreateBook(services_pb2.CreateBookRequest(book=bookrequest))
            return response
        return "ERROR, SERVER DOWN"

    def GetBook(self, ISBN):
        with grpc.insecure_channel(self.server) as channel:
            stub = services_pb2_grpc.InventoryServiceStub(channel)
            response = stub.GetBook(services_pb2.GetBookRequest(book=ISBN))
            return response
        return "ERROR, SERVER DOWN"


if __name__ == "__main__":
    print("FILE IS EXECUTING")
    inventory_object = inventory_client(ip="localhost", port="50051")
    print(data.books[0])
    print(inventory_object.CreateBook(book=data.books[0]))
    print(inventory_object.GetBook(ISBN="2"))
