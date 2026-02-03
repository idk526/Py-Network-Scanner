import urllib.request
import urllib.error
import sys

# Target URL (Using a safe test site or localhost)
base_url = "http://127.0.0.1" 

# Common hidden directories to look for (The "Wordlist")
paths_to_check = [
    "admin",
    "login",
    "config",
    "backup",
    "dashboard",
    "api",
    "aws",
    "cloud"
]

print(f"[*] Starting Directory Enumeration on: {base_url}")
print("-" * 50)

try:
    for path in paths_to_check:
        url = f"{base_url}/{path}"
        try:
            # Send a request to the URL
            response = urllib.request.urlopen(url)
            
            # If we get a 200 OK code, the directory exists
            if response.getcode() == 200:
                print(f"[+] FOUND: {url} (Status: 200)")
                
        except urllib.error.HTTPError as e:
            # 403 means "Forbidden" (It exists but is private) - This is a good find!
            if e.code == 403:
                print(f"[!] FORBIDDEN (Exists): {url} (Status: 403)")
            # 404 means "Not Found", so we ignore it
            pass
        except urllib.error.URLError:
            print("[-] Connection Failed. Target may be down.")
            break

except KeyboardInterrupt:
    print("\n[!] Scan Aborted.")

print("-" * 50)
print("[*] Scan Complete.")
