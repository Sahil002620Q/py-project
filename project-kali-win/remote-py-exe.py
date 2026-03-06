import paramiko

def run_kali_command(command):
    # --- Configuration ---
    host = "127.0.0.1"  # Replace with your Kali Linux IP
    username = "kali"      # Your Kali username
    password = "sahil999n" # Your Kali password

    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        # Automatically add the remote server's SSH key
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to Kali
        client.connect(hostname=host, username=username, password=password)
        
        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)
        
        # Read the output
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(f"--- Output ---\n{output}")
        if error:
            print(f"--- Error ---\n{error}")

        client.close()
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    cmd = input("Enter Kali command to run: ")
    run_kali_command(cmd)

    #h@c|< kali inderictly run < sudo systemctl start ssh > on kali and run this program and replace ip and user pass