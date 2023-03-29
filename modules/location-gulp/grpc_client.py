import grpc
import faker
import location_pb2
import location_pb2_grpc

print("sending payload sample ... ... ...")

channel = grpc.insecure_channel("127.0.0.1:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

preloaded_person_ids = [1, 2, 5, 8, 9]
non_existing_person_ids = [879, 45]

fake = faker.Faker()

def randomFloatStr():
    return str(fake.pyfloat(1))

# Send the desired payload to existing and non-existing people
payloads_list = [
    location_pb2.LocationMessage(person_id=b, latitude=randomFloatStr(), longitude=randomFloatStr()) for a in [preloaded_person_ids, non_existing_person_ids] for b in a
    ]

for location in payloads_list:
    response = stub.Create(location)
    print(f"Response from gRPC server: {response}")