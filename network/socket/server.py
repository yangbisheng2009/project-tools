import socket
import sys
from time import ctime
import argparse
import traceback
import time


parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='0.0.0.0', help='指定可容忍的客户端ip')
parser.add_argument('--port', type=int, default=8089, help='端口号')
parser.add_argument('--buff-len', type=int, default=1024, help='通信buff的长度')
args = parser.parse_args()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((args.host, args.port))
    server_socket.listen()

    while True:
        try:
            # Step1. 接收连接，读取消息
            # =====================================
            conn, addr = server_socket.accept()
            print('connection ip: {}'.format(addr))
            data = conn.recv(args.buff_len)
            print(data, time.time())
            # =====================================

            # Step2. 可选，给client发送一个消息
            # =====================================
            msg = 'I get your msg: %s' % data.decode()
            conn.send(msg.encode())
            conn.close()
            # =====================================
        except:
            traceback.print_exc()

    server_socket.close()


if __name__ == '__main__':
    start_server()