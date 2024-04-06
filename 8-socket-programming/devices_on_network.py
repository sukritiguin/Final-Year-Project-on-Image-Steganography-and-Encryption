import socket
import subprocess

def discover_devices():
    # Run the 'arp -a' command to get a list of devices on the local network
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    
    # Extract IP addresses from the command output
    devices = []
    for line in result.stdout.split('\n'):
        parts = line.split()
        if len(parts) >= 2:
            ip_address = parts[0]
            devices.append(ip_address)
    
    return devices

# Example usage:
devices = discover_devices()
print("Devices on the network:")
for device in devices:
    print(device)
