import socket

def lookup(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connection
    s.connect(("whois.iana.org", 43))
    # Request
    s.send(f"{domain}\r\n".encode())
    # Information retrieved
    response = my_socket.recv(4096).decode()
    s.close()
    return response

site = input("What site would you like to look up? ")
print(lookup(site))
