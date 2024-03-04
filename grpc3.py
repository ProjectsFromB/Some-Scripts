import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = grpc.UnaryStub(channel)

response = stub.SayHello(HelloRequest(name='world'))
print(response.message)
