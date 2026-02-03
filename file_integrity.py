import hashlib
import os

def calculate_sha256(file_path):
    """Reads a file and returns its SHA-256 hash."""
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            # Read the file in 4K chunks to be memory efficient
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

# --- Main Execution ---
if __name__ == "__main__":
    # Create a dummy file to test the script
    test_filename = "cloud_config_test.txt"
    with open(test_filename, "w") as f:
        f.write("Do not allow public access to this bucket.")

    print(f"[*] Integrity Monitor Started...")
    print(f"[*] Target File: {test_filename}")
    
    # Calculate Hash
    file_hash = calculate_sha256(test_filename)
    
    if file_hash:
        print(f"[+] Current SHA-256 Hash: {file_hash}")
        print("-" * 60)
        print("Copy this hash. If the file content changes even slightly,")
        print("this hash will change completely (Avalanche Effect).")
        print("-" * 60)
    else:
        print("[-] Error: File not found.")

    # Clean up (remove test file)
    # os.remove(test_filename)
