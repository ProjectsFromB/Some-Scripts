import grpc
import myservice.proto
import myservice.proto_grpc

def run_grpc_client():
    # Define the server address and port
    server_address = '10.10.11.214:50051'

    # Create a gRPC channel
    channel = grpc.insecure_channel(server_address)

    # Create a gRPC stub
    stub = myservice.proto_grpc.YourServiceStub(channel)

    try:
        # Create a request object
        request = myservice.proto.YourRequest()
        request.message = 'Hello, gRPC!'

        # Call the gRPC method
        response = stub.YourRPCMethod(request)

        # Process the response
        print('Response:', response.reply)

    except grpc.RpcError as e:
        # Handle gRPC errors
        print('Error:', e.details())

    # Close the gRPC channel
    channel.close()

if __name__ == '__main__':
    run_grpc_client()

