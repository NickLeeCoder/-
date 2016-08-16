import socket

# 这是一个 web 服务器

host = ''
port = 2000

# 新建 socket
# bind 绑定服务器的 host 和 port
s = socket.socket()
s.bind((host, port))


def read_from_file(filename):
    with open(filename, 'rb') as f:
        return f.read()


# 用一个无限循环来接受请求
while True:
    # 用 listen 监听请求
    s.listen(5)
    connection, address = s.accept()

    # 用 recv 接收客户端发送的请求数据
    request = connection.recv(1024)
    request = request.decode('utf-8')

    print('ip and request, {}\n{}'.format(address, request))
    line = request.split('\n')[0]
    print('line', line)
    path = line.split()[1]
    print('path, ', path)
    # 用 sendall 把响应数据发送给客户端
    response = b'Hello lwk!'
    connection.sendall(response)

    # 用 close 关闭连接
    connection.close()
