import json
import logging
import sys
from concurrent import futures

import grpc
import inventory_client


def getBooks(client, ISBNs):
    books = []
    for ISBN in ISBNs:
        book = client.GetBook(ISBN=ISBN)
        print(book.book.title)
        books.append(book.book.title)
    return books


if __name__ == "__main__":
    ISBNs = ["1","2"]
    client = inventory_client.inventory_client(ip="localhost", port="50051")
    titles = getBooks(client=client, ISBNs=ISBNs)
    print(titles)