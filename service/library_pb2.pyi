from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishingYear", "title"]
    class genres(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CLASSICS: Book.genres
    FANTASY: Book.genres
    GENRE_FIELD_NUMBER: _ClassVar[int]
    HUMOR: Book.genres
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    SCIFI: Book.genres
    TITLE_FIELD_NUMBER: _ClassVar[int]
    WAR: Book.genres
    author: str
    genre: Book.genres
    publishingYear: Date
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.genres, str]] = ..., publishingYear: _Optional[_Union[Date, _Mapping]] = ...) -> None: ...

class Date(_message.Message):
    __slots__ = ["day", "month", "year"]
    DAY_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    day: int
    month: int
    year: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["b", "inventoryNumber", "status"]
    class statuses(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.statuses
    B_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.statuses
    b: Book
    inventoryNumber: int
    status: InventoryItem.statuses
    def __init__(self, inventoryNumber: _Optional[int] = ..., b: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.statuses, str]] = ...) -> None: ...
