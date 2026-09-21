"""
Dharma Protocol
Canonical DRFC Reference
Status: Traceability Pending
"""

import socket
import threading
import time

from dharma.network.transport import Transport


def test_endpoint():
    assert Transport().endpoint() == "127.0.0.1:4040"


def test_host():
    assert Transport().host == "127.0.0.1"


def test_port():
    assert Transport().port == 4040


def test_server_client_echo():
    t = Transport(port=4041)
    server = t.server()

    def run():
        conn, _ = server.accept()
        data = conn.recv(1024)
        conn.sendall(data)
        conn.close()
        server.close()

    threading.Thread(target=run, daemon=True).start()
    time.sleep(0.1)

    client = t.client()
    client.sendall(b"Dharma")
    assert client.recv(1024) == b"Dharma"
    client.close()


def test_invalid_connect():
    t = Transport(port=4999)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((t.host, t.port))
        assert False
    except OSError:
        assert True
    finally:
        s.close()


def test_custom_endpoint():
    assert Transport(port=5050).endpoint() == "127.0.0.1:5050"


def test_server_socket():
    s = Transport(port=4042).server()
    assert s.fileno() != -1
    s.close()


def test_multiple_connections():
    t = Transport(port=4043)
    server = t.server()

    def run():
        for _ in range(2):
            conn, _ = server.accept()
            conn.sendall(b"ok")
            conn.close()
        server.close()

    threading.Thread(target=run, daemon=True).start()
    time.sleep(0.1)

    for _ in range(2):
        c = t.client()
        assert c.recv(2) == b"ok"
        c.close()


def test_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    assert s.gettimeout() == 0.5
    s.close()


def test_custom_host():
    assert Transport(host="localhost").host == "localhost"


def test_endpoint_format():
    assert ":" in Transport().endpoint()
