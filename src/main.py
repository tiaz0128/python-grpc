import route_guide_pb2 as pb2
from google.protobuf.json_format import MessageToJson, Parse

person = pb2.Person()
person.name = "Tiaz0128"

serialized = person.SerializeToString()
assert isinstance(serialized, bytes)

new_person = pb2.Person()
new_person.ParseFromString(serialized)

print(new_person.name)
