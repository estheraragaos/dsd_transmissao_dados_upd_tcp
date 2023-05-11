import socket


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = "192.168.2.14" # endereço IP do servidor
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = "0"

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            self.client.sendto(str.encode(data), self.addr)
            reply, server_address = self.client.recvfrom(2048)
            return reply.decode()
        except socket.error as e:
            return str(e)
