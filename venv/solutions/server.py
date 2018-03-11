import socket

result = '''ok\npalm.cpu 10 1111\nsmalm.cpu 10 222\npalm.cpu 12 1111\npalm.cpu 13 1111\n\n'''
with socket.socket() as sock:
    sock.bind(('127.0.0.1', 10001))
    sock.listen()
    while True:
        conn, adr = sock.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode('utf8'))
                conn.send(result.encode('utf8'))

