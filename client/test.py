import json
import logging
import sys
from concurrent import futures
from unittest.mock import MagicMock

import get_book_titles
import grpc
import inventory_client


class dotdict(dict):
    """dot.notation access to dictionary attributes to effectively mock a Book object"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def side_effects(ISBN):
    """Support function for the mock to return pseudo-book object"""
    bookname = "book" + str(ISBN)
    title = dotdict({"title" : bookname})
    book = { "book" : title }
    book = dotdict(book)
    return book


def test_Mock():
    # Create mock of client class and mock the getbook function with a side_effect
    client = MagicMock(side_effect = side_effects)
    client.GetBook = MagicMock(side_effect = side_effects)

    # List of ISBNs to fetch books
    ISBNs = ["1","2"]

    # Call getBooks containing mocked client
    titles = get_book_titles.getBooks(client=client, ISBNs=ISBNs)

    # Verify book titles
    assert titles == ['book1', 'book2']


def test_Server():
    # Establish client object and connection to server
    client = inventory_client.inventory_client(ip="localhost", port="50051")

    # List of ISBNs to fetch books
    ISBNs = ["1","2"]

    # Call getBooks to fetch books frmo actual server
    titles = get_book_titles.getBooks(client=client, ISBNs=ISBNs)
    
    # Verify book titles
    assert titles == ['book1', 'book2']

if __name__ == "__main__":
    test_Mock()
    test_Server()