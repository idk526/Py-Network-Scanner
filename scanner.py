import socket
import sys
from datetime import datetime

# Target Definition
target = "127.0.0.1" # Default to localhost for safety

# Banner
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    # Scan ports 1 to 100 (Common ports)
    for port in range(1, 100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        # Returns 0 if connection is successful
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        s.close()
        
except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()
