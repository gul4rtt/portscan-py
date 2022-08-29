#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # hostname para ipv4
else:
    print("Você provavelmente esqueceu de passar os argumentos...\nmodo de uso: ./scanner.py <ip>")
    quit()

print("-" * 50)
print(f"Alvo definido como: {target}")
print(f"tempo de inicio: {str(datetime.now())}")
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # tempo de tentativa de conexão
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"port {port} is open.")
        s.close()

except KeyboardInterrupt
    print("\nInterrompendo execução...")
    sys.exit()

except socket.gaierror:
    print("O host não pode ser resolvido...")
    sys.exit()

except socket.error:
    print("Não foi possível a conexão com o servidor...")
    sys.exit()

