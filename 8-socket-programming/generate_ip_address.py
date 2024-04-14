import subprocess
import re

def get_wireless_ipv4():
    # Run the ipconfig command
    result = subprocess.run(['ipconfig'], capture_output=True, text=True)

    # Extract IPv4 addresses from the output
    matches = []
    if result.returncode == 0:
        output = result.stdout
        # Use regular expression to find the IPv4 addresses
        matches = re.findall(r"IPv4 Address[.\s]+: ([0-9]+(?:\.[0-9]+){3})", output)
    return matches
matches = get_wireless_ipv4()
print(matches)