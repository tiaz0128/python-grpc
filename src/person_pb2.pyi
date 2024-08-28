from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Person(_message.Message):
    __slots__ = ("name", "age", "gender", "hobbies", "address")
    class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Person.Gender]
        MALE: _ClassVar[Person.Gender]
        FEMALE: _ClassVar[Person.Gender]
    UNKNOWN: Person.Gender
    MALE: Person.Gender
    FEMALE: Person.Gender
    class Address(_message.Message):
        __slots__ = ("street", "city")
        STREET_FIELD_NUMBER: _ClassVar[int]
        CITY_FIELD_NUMBER: _ClassVar[int]
        street: str
        city: str
        def __init__(self, street: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    HOBBIES_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    gender: Person.Gender
    hobbies: _containers.RepeatedScalarFieldContainer[str]
    address: Person.Address
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ..., gender: _Optional[_Union[Person.Gender, str]] = ..., hobbies: _Optional[_Iterable[str]] = ..., address: _Optional[_Union[Person.Address, _Mapping]] = ...) -> None: ...
