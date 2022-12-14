import json
import logging
import sys
from concurrent import futures

import grpc
import inventory_client


def getBooks(client, ISBNs):
    # Fetches all books for given list of ISBNs
    books = []
    for ISBN in ISBNs:
        # retrieve a book using GetBook function
        book = client.GetBook(ISBN=ISBN)
        # Add to list
        books.append(book.book.title)
    return books


if __name__ == "__main__":
    # Main class to test the getBooks function
    ISBNs = ["1","2"]
    # Create a client encapsulation object
    client = inventory_client.inventory_client(ip="localhost", port="50051")
    # Get book titles for mentioned ISBNs
    titles = getBooks(client=client, ISBNs=ISBNs)
    print(titles)