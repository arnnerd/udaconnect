from concurrent import futures
from helper import publish_set_location

import grpc
import location_pb2
import location_pb2_grpc



class LocationGulpServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        payload = {
            "person_id": int(request.person_id),
            "latitude": request.latitude,
            "longitude": request.longitude
        }

        print(f"Payload: {payload} ")

        publish_set_location(payload)
        return location_pb2.LocationMessage(**payload)
    
# Intiialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationGulpServicer(), server)

print("Starting gRPC server on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

# Keep thread alive
server.wait_for_termination()
# try:
#     while True:
#         time.sleep(86400)
# except KeyboardInterrupt:
#     server.stop(0)