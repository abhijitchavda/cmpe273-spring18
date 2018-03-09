# chat application using ZeroMQ 
### How to Setup

```sh
virtualenv -p python3 my-venv
. my-venv/bin/activate
pip3 install -r requirements.txt
```

### How to run Chat server

```sh
python3 chat_server.py
```

### How to run a Chat client

```sh
python3 chat_client.py [username]
```

__Expected Output__

# Bob's client
```sh
python3 chat_client.py Bob
User [Bob] Connected to the server.
hi
[Alice]: Hi from Alice.
[Smith]: Hi from Smith.
Hello World
```

# Alice's client
```sh
python3 chat_client.py Alice
User[ Alice] Connected to the chat server. 
[Bob]:hi
Hi from Alice.
[Smith]: Hi from Smith.
[Bob]: Hello World
```


# smith's client
```sh
python3 chat_client.py smith
User [smith] Connected to the chat server. 
[Bob]:hi
[Alice]:Hi from Alice.
Hi from Smith.
[Bob]: Hello World
```
