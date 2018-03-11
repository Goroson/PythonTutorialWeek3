import socket
import json
import time
import re

class ClientError(Exception):
    def __init__(self, expression, message):
        self.message = message
        self.expression = expression
        self.connection = None


class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout

    def get(self, request):
        self.get_connection()
        self.connection.sendall(request.encode('utf8'))
        # get data
        received_data= (self.connection.recv(1024).decode('utf8'))
        data = self.process_data_from_server(received_data)
        return data

    def put(self, key, value, timestamp=str(time.time())):
        data = 'put {0} {1} {2}\n'.format(key, value, timestamp)
        self.get_connection()
        try:
            self.connection.sendall(data)
        except:
            raise ClientError

    def get_connection(self):
        self.connection = socket.socket()
        try:
            self.connection.connect((self.ip, self.port))
        except ConnectionError:
            raise ClientError


    def close_connection(self):
        self.connection.close()

    def process_data_from_server(self, data):
        dict = {}
        if re.finditer(r'ok.+\n\n', data):
            for line in re.finditer(r"[^\n]{3,}", data):
                print(line.group(0))
                line = line.group(0).split(' ')
                if line[0] not in dict:
                    dict[line[0]] = []
                dict[line[0]].append((int(line[1]), int(line[2])))

            print(str(dict))
        else:
            raise ClientError

        return dict

