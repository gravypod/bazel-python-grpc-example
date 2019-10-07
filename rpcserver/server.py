import time
from concurrent import futures
from os import getenv

import grpc

from specs import greeter_grpc


class GreeterService(greeter_grpc.GreeterBase):
    pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_grpc.add_GreeterService_to_server(GreeterService(), server)
    port = getenv('SERVER_PORT', '50076')
    server.add_insecure_port('[::]:' + port)
    print("Python RouteGuide Server listening on :%s..." % port)
    server.start()
    try:
        while True:
            time.sleep(512)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
