import sys, os, select, socket, ssl, urllib

if __name__ == "__main__":

    host = sys.argv[1]
    port = int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    context.load_default_certs()
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
    context.options |= ssl.OP_NO_TLSv1
    context.options |= ssl.OP_NO_TLSv1_1
    context.options |= ssl.OP_NO_TLSv1_3
    
    ssl_sock = context.wrap_socket(s, server_side=False, do_handshake_on_connect=True, suppress_ragged_eofs=True)
    try:
        ssl_sock.connect((host, port))
    except ssl.SSLError:
        print ("Failed to connect without TLSv1 and TLSv3")
    else:
        print ("Success: Socket Version: " + ssl_sock.version())
        assert ssl_sock.version() == "TLSv1.2"
    s.close()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    context.load_default_certs()
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
    context.options |= ssl.OP_NO_TLSv1
    context.options |= ssl.OP_NO_TLSv1_1
    context.options |= ssl.OP_NO_TLSv1_2
    
    ssl_sock = context.wrap_socket(s, server_side=False, do_handshake_on_connect=True, suppress_ragged_eofs=True)
    try:
        ssl_sock.connect((host, port))
    except ssl.SSLError:
        print ("Failed to connect without TLSv1 and TLSv2")
    else:
        print ("Success: Socket Version: " + ssl_sock.version())
        assert ssl_sock.version() == "TLSv1.3"
    s.close()
