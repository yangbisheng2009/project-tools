import socket
import argparse
import time
import traceback


parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default='localhost', help='指定可容忍的客户端ip')
parser.add_argument('--port', type=int, default=8089, help='端口号')
parser.add_argument('--buff-len', type=int, default=1024, help='通信buff的长度')
args = parser.parse_args()


def pkg_msg():
    pass


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((args.host, args.port))

    try:
        # Step1.发送消息
        # =====================================
        msg = pkg_msg()
        client_socket.send(msg.encode())
        # =====================================

        # Step2.可选，接收消息
        # =====================================
        data = client_socket.recv(args.buff_len)
        print(data, time.time())
        # =====================================

        client_socket.close()
    except:
        traceback.print_exc()


if __name__ == '__main__':
    start_client()