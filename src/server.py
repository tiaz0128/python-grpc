import grpc
from concurrent import futures
import person_pb2
import route_guide_pb2
import route_guide_pb2_grpc


class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    def __init__(self):
        self.people = {
            "Alice": person_pb2.Person(
                name="Alice",
                age=30,
                gender=person_pb2.Person.FEMALE,
                hobbies=["reading", "swimming"],
                address=person_pb2.Person.Address(
                    street="123 Main St", city="New York"
                ),
            ),
            "Bob": person_pb2.Person(
                name="Bob",
                age=25,
                gender=person_pb2.Person.MALE,
                hobbies=["gaming", "cycling"],
                address=person_pb2.Person.Address(
                    street="456 Elm St", city="Los Angeles"
                ),
            ),
        }

    def GetPerson(self, request, context):
        name = request.name
        return self.people.get(name, person_pb2.Person(name="Not Found"))

    def GetPeople(self, request_iterator, context):
        for name_request in request_iterator:
            person = self.people.get(name_request.name)
            if person:
                yield person


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(), server)
    server.add_insecure_port("[::]:50051")
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
