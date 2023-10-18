import configparser
import subprocess
import sys

def copy_ssh_key_to_hosts(username, ini_file_path):
    # Parse the INI file
    config = configparser.ConfigParser()
    config.read(ini_file_path)
    
    # Get list of hosts from the INI file
    if 'hosts' not in config:
        print("No 'hosts' section found in the INI file.")
        return

    hosts = config['hosts'].get('list', '').split(',')
    
    for host in hosts:
        host = host.strip()
        if not host:
            continue
        
        # Run the ssh-copy-id command
        cmd = ['ssh-copy-id', f'{username}@{host}']
        try:
            subprocess.run(cmd, check=True)
            print(f'SSH key copied to {host} successfully.')
        except subprocess.CalledProcessError:
            print(f'Failed to copy SSH key to {host}.')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 script_name.py <username> <path_to_ini_file>")
        sys.exit(1)
    
    username = sys.argv[1]
    ini_file_path = sys.argv[2]
    
    copy_ssh_key_to_hosts(username, ini_file_path)
