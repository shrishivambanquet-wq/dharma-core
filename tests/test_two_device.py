import socket
import threading
import time

from dharma.network.server import DharmaServer
from dharma.network.client import DharmaClient

def test_local_exchange():
    temp = socket.socket()
    temp.bind(("127.0.0.1", 0))
    port = temp.getsockname()[1]
    temp.close()

    server = DharmaServer(host="127.0.0.1", port=port)

    t = threading.Thread(target=server.serve_once)
    t.start()

    time.sleep(0.2)

    reply = DharmaClient().connect("127.0.0.1", port)

    t.join()

    assert reply["reply"] == "hello_from_dharma"
