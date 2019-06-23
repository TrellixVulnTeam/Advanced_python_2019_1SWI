import yaml, json
import socket
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
)

args = parser.parse_args()

host = '0.0.0.0'
port = 8000
buffersize = 1024
encoding = 'utf-8'

if args.config:
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.Loader)
        host = config.get('host')
        port = config.get('port')


try:
    sock = socket.socket()

    sock.bind((host, port))
    sock.listen(5)
    print(f'Server was started with {host}:{port}')

    while True:
        client, address = sock.accept()
        
        b_request = client.recv(buffersize)
        request = json.loads(b_request.decode(encoding))
        
        action_name = request.get('action')

        # if action_name == 'echo':
        #     pass
        # elif action_name:


        client.send(data)
        client.close()
except KeyboardInterrupt:
    pass
