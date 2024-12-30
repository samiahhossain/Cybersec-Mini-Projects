import socket

def lookup(domain: str):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect(("whois.iana.org", 43))
    my_socket.send(f"{domain}\r\n".encode())
    response = my_socket.recv(4096).decode()
    my_socket.close()
    return response

site = input("What site would you like to look up? ")
print(lookup(site))
