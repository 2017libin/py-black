from audioop import add
from calendar import c
from distutils.command.clean import clean
import socket
from urllib import response

def client_tcp(host:str, port:str):
    # 创建一个tcp客户端
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 建立连接
    client.connect((host,port))
    
    # 发送数据
    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    
    # 获取响应
    response = client.recv(4096)

    print(response.decode())
    
    # 关闭连接z
    client.close()
    
def client_udp(host:str, port:str):
    
    # 创建一个tcp客户端
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 发送数据
    client.sendto(b"AAABBBCCC", (host,port))
    
    # 获取响应
    data, addr = client.recvfrom(4096)

    print(addr)
    print(data.decode())
    
    # 关闭连接
    client.close()

if __name__ == "__main__":
    target_host = "127.0.0.1"
    target_port = 9997
    client_udp(target_host,target_port)