import io
import socket
import sys


class WSGIServer:
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        # Initializes the listening socke
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )


        # Sets socket option of reusing address at level of sol_socket(socket level) to 1 (True)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Binds address to socket
        listen_socket.bind(server_address)
        # Listen to (request size) amount of requests
        listen_socket.listen(self.request_queue_size)

        # Gets server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        # Get fully qualified domain name
        self.server_name = socket.getfqdn(host)
        self.server_port = port

        self.headers_set = []

