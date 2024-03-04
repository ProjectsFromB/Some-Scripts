import grpc
from helloworld_pb2 import HelloRequest
from helloworld_pb2_grpc import GreeterStub

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = GreeterStub(channel)

    response = stub.SayHello(HelloRequest(name='world'))
    print(response.message)

if __name__ == '__main__':
    main()

