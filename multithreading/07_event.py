import random
import time
from enum import Enum
from threading import Thread, Event


class BankTerminal:
    def __init__(self, port, ip_address):
        self.ip_address = ip_address
        self.port = port
        self.protocol = Protocol(port, ip_address)
        self.protocol.message_received += self.on_message_received
        self.operation_signal = Event()

    def on_message_received(self, status):
        print(f"signaling with {status} \n")
        self.operation_signal.set()

    def purchase(self, amount):
        def process_purchase():
            op_code = 1
            self.protocol.send(op_code, amount)
            self.operation_signal.clear()
            print(f"wait.. \n")
            self.operation_signal.wait()
            print("purchase finished \n")

        t = Thread(target=process_purchase)
        t.start()
        return t


class Event_temp:
    def __init__(self):
        self.handlers = []

    def __call__(self, *args, **kwargs):
        for f in self.handlers:
            f(*args, **kwargs)

    def __iadd__(self, other):
        self.handlers.append(other)
        return self

    def __isub__(self, other):
        self.handlers.remove(other)
        return self


class OperationStatus(Enum):
    FINISHED = 0
    FAULTED = 1


class Protocol:
    def __init__(self, port, ip_address):
        self.ip_address = ip_address
        self.port = port
        self.message_received = Event_temp()
        self.set_ip()

    def set_ip(self):
        print("set ip and port \n")
        time.sleep(0.2)
        return

    def send(self, op_code, param):
        def process_sending():
            print(f"operation send with param:{param}\n")
            result = self.process(op_code, param)
            self.message_received(result)

        t = Thread(target=process_sending)
        t.start()

    def process(self, op_code, param):
        print(f"process {op_code} with {param} \n")
        time.sleep(3)
        fin = random.randint(0, 1) == 1
        return OperationStatus.FINISHED if fin else OperationStatus.FAULTED


if __name__ == "__main__":
    bt = BankTerminal(10, "192.168.0.1")
    t = bt.purchase(20)
    t.join()
    t = bt.purchase(30)
    t.join()
