import logging
from concurrent import futures

import data
import grpc
import library_pb2
import library_pb2_grpc
import services_pb2
import services_pb2_grpc


def CreateBookResponse(b):
        book = library_pb2.Book()
        book.ISBN = b.book.ISBN
        book.title = b.book.title
        book.author = b.book.author
        book.genre = b.book.genre
        book.publishingYear.year= b.book.publishingYear.year
        return book

def CreateBookFromDatabase(b):
    book = library_pb2.Book()
    book.ISBN = b["ISBN"]
    book.title = b["title"]
    book.author = b["author"]
    book.genre = b["genre"]
    book.publishingYear.year= b["publishingYear"]
    return book


class Inventory(services_pb2_grpc.InventoryServiceServicer):


    def CreateBook(self, request, context):
        print(request.book)
        book = CreateBookResponse(request)
        print(book)
        data.books.append({'ISBN': book.ISBN, 'title': book.title, 'author': book.author, 'genre': book.genre, 'publishingYear': book.publishingYear.year})
        print(data.books)
        return services_pb2.CreateBookResponse(book=book)

    def GetBook(self, request, context):
        print(request.book)
        book = [b for b in data.books if b["ISBN"]==request.book][0]
        print(book)
        bookresponse = CreateBookFromDatabase(book)
        print(bookresponse)
        return services_pb2.GetBookResponse(book=bookresponse)
        


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_InventoryServiceServicer_to_server(Inventory(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()