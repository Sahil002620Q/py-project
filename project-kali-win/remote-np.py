import paramiko
import os
import sys

# --- SETTINGS ---
# Run 'ip a' in Kali and put that IP here
KALI_IP = "127.0.0.1" 
KALI_USER = "kali"

def run_remote_control():
    # This finds the folder where your .exe or .py is running
    base_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
    config_path = os.path.join(base_dir, "config.txt")

    # 1. Create the 'Control Panel' file if it's missing
    if not os.path.exists(config_path):
        with open(config_path, "w") as f:
            f.write("# Enter your Kali command on the line below\nls -la")
        print(f"[*] Created: {config_path}")
        print("[*] Open this file, type your command, save it, and run this program again.")
        return

    # 2. Read your desired command from the text file
    with open(config_path, "r") as f:
        lines = f.readlines()
        # Filter out comments starting with # and empty lines
        command_to_run = "".join([l for l in lines if not l.startswith("#")]).strip()

    if not command_to_run:
        print("[!] config.txt is empty. Please enter a command.")
        return

    try:
        # 3. Setup the SSH Connection (using your SSH keys)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        print(f"[*] Connecting to {KALI_IP}...")
        # No password needed because of your id_rsa.pub key!
        client.connect(hostname=KALI_IP, username=KALI_USER)
        
        print(f"[*] Executing from config.txt: {command_to_run}")
        stdin, stdout, stderr = client.exec_command(command_to_run)
        
        # 4. Stream the results back to your VS Code terminal
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print("\n--- KALI OUTPUT ---")
            print(output)
        if error:
            print("\n--- ERROR LOG ---")
            print(error)

        client.close()
    except Exception as e:
        print(f"[!] Connection failed: {e}")
        print("[*] Make sure Kali is on and you have the right IP.")

if __name__ == "__main__":
    run_remote_control()
    input("\nFinished. Press Enter to close...")