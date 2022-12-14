import logging
from concurrent import futures

import data
import grpc
import library_pb2
import library_pb2_grpc
import services_pb2
import services_pb2_grpc


def CreateBookResponse(b):
    # This function is used to create a CreateBookResponse object from a CreateBookRequest
    # This function can also be used to validate the sent book object
    book = library_pb2.Book()
    book.ISBN = b.book.ISBN
    book.title = b.book.title
    book.author = b.book.author
    book.genre = b.book.genre
    book.publishingYear.year= b.book.publishingYear.year
    return book

def CreateBookFromDatabase(b):
    # This function is used to create a Book message object from a database entry.
    book = library_pb2.Book()
    book.ISBN = b["ISBN"]
    book.title = b["title"]
    book.author = b["author"]
    book.genre = b["genre"]
    book.publishingYear.year= b["publishingYear"]
    return book


class Inventory(services_pb2_grpc.InventoryServiceServicer):


    def CreateBook(self, request, context):
        # Create a response object from the given book
        book = CreateBookResponse(request)
        # Add book to the database
        data.books.append({'ISBN': book.ISBN, 'title': book.title, 'author': book.author, 'genre': book.genre, 'publishingYear': book.publishingYear.year})
        # send the validated new book object as a newly created book for validation frmo the client-side
        return services_pb2.CreateBookResponse(book=book)

    def GetBook(self, request, context):
        # Find the book with the corresponding ISBN
        book = [b for b in data.books if b["ISBN"]==request.book][0]
        # Create a Book object from the database entry
        bookresponse = CreateBookFromDatabase(book)
        # Send Book object encapsulated in the response
        return services_pb2.GetBookResponse(book=bookresponse)
        


def serve():
    # Function to initialize and run the server
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