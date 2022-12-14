import json
import logging
import sys
from concurrent import futures
from unittest.mock import MagicMock

import get_book_titles
import grpc
import inventory_client


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def side_effects(ISBN):
    bookname = "book" + str(ISBN)
    title = dotdict({"title" : bookname})
    book = { "book" : title }
    book = dotdict(book)
    return book


def test_Mock():
    client = MagicMock(side_effect = side_effects)
    client.GetBook = MagicMock(side_effect = side_effects)

    ISBNs = ["1","2"]

    titles = get_book_titles.getBooks(client=client, ISBNs=ISBNs)

    assert titles == ['book1', 'book2']


def test_Server():
    client = inventory_client.inventory_client(ip="localhost", port="50051")

    ISBNs = ["1","2"]

    titles = get_book_titles.getBooks(client=client, ISBNs=ISBNs)
    
    assert titles == ['book1', 'book2']

# if __name__ == "__main__":
#     test_Mock()
#     test_Server()