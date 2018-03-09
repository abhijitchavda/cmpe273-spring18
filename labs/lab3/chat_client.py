import zmq
import select
import sys
import json
from threading import Thread
import time

context = zmq.Context()

socket_sub = context.socket(zmq.SUB)
socket_sub.setsockopt_string(zmq.SUBSCRIBE,"")
socket_sub.connect("tcp://127.0.0.1:5678")
socket_req = context.socket(zmq.REQ)
socket_req.connect("tcp://127.0.0.1:5680")

def subscriber(name):
    while True:
        while True:
            try:
                message=json.loads(socket_sub.recv_string(zmq.NOBLOCK))
                if message['name'] != name:
                    sys.stdout.write("[%s]: %s" % (message['name'], message['message']))
                print("\n")
            except zmq.ZMQError:
                break
        
        time.sleep(0)
        


def sender(name):
    while True:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            message=str(sys.stdin.readline())
        else:
            message="1"
        if message != "1" :
            socket_req.send_string(json.dumps({
            'name': name,
            'message': message,
        }))
            msg = str(socket_req.recv_string())
        
        time.sleep(0)


if __name__ == '__main__':
    name = sys.argv[1]
    print("user [%s] connected to the server" % (name))
    sender=Thread(target=sender,args=(name,))
    subscriber=Thread(target=subscriber,args=(name,))
    sender.start()
    subscriber.start()
    sender.join()
    subscriber.join()
