import person_pb2

person = person_pb2.Person()
person.name = "John Doe"

serialized = person.SerializeToString()
assert isinstance(serialized, bytes)

new_person = person_pb2.Person()
new_person.ParseFromString(serialized)

print(new_person.name == person.name)
