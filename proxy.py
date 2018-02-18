import tornado
import socket
def get(self):

    def write_to_server(data):
        req_stream.write(data)
    def req_close(data):
        if conn_stream.closed():
            return
        else:
            conn_stream.write(data)
    def write_to_cilent(data):
        req_stream.write(data)
    def proxy_close(data):
        if req_stream.closed():
            return
        else:
            req_stream.close(data)
            return
    def on_connect():
        req_stream.read_untill_close(req_close,write_to_server)
        conn_stream.read_untill_close(proxy_close,write_to_cilent)
        req_stream.write(b'Server OK ,Proxy started.')


    print('Preload OK,Starting connnect to %s' %self.request.uri)
    req_stream = self.request.connection.stream

    host,port = (None,443)
    print('+--------------------Proxy Settings--------------------+')
    host = raw_input('Host (Default is none)>')
    port = raw_input('Port (Default is 443)>')
    int(port)
    print ('Proxy on '+host+' '+port)
    netloc = self.request.uri.split(':')
    if len(netloc) == 1:
        host,port = netloc[0]
    elif len(netloc) == 2:
        host,port = netloc

    s = socket(socket.AF_INET,socket.SOCK_STREAM,0)
    conn_stream = torando.iostream.IOstream(s)
    conn_stream.connect((host,port),on_connect)




