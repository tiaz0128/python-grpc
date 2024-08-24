import pytest

import src.person_pb2 as person_pb2


class TestProtoPerson:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Person 객체 생성
        self.person = person_pb2.Person()
        self.person.name = "John Doe"

        # PersonWrapper 객체 생성
        self.wrapper = person_pb2.PersonWrapper()
        self.wrapper.person.CopyFrom(self.person)

    def test_serialization(self):
        result = self.wrapper.SerializeToString()

        assert isinstance(result, bytes)

    def test_deserialization(self):
        serialized = self.wrapper.SerializeToString()

        new_wrapper = person_pb2.PersonWrapper()
        new_wrapper.ParseFromString(serialized)

        assert new_wrapper.person.name == self.person.name
