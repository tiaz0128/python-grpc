import grpc
import route_guide_pb2
import route_guide_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)

        # GetPerson 호출
        name = route_guide_pb2.Name(name="Alice")
        person = stub.GetPerson(name)
        print(
            f"GetPerson: {person.name}, Age: {person.age}, Gender: {person.gender}, "
            f"Hobbies: {person.hobbies}, Address: {person.address.street}, {person.address.city}"
        )

        # GetPeople 호출
        names = [
            route_guide_pb2.Name(name="Alice"),
            route_guide_pb2.Name(name="Bob"),
            route_guide_pb2.Name(name="Charlie"),
        ]
        people = stub.GetPeople(iter(names))
        for person in people:
            print(
                f"GetPeople: {person.name}, Age: {person.age}, Gender: {person.gender}, "
                f"Hobbies: {person.hobbies}, Address: {person.address.street}, {person.address.city}"
            )


if __name__ == "__main__":
    run()
