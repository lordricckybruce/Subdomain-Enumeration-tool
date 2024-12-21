#!/bin/python3

import sys   #handles command line argument 
import os   #check file existence
import socket   # for network connection and also resolve DNS
from concurrent.futures import ThreadPoolExecutor    #enable concurrent processing

def resolve_subdomain(domain, subdomain):  # definde the function resolve_subdomain
'''
contruct full subdomain 
return ip if found
uses socket.gethostbyname to resolve  the subdomain to an ip
'''
    """Attempts to resolve a subdomain."""
    try:
        full_domain = f"{subdomain}.{domain}"
        ip = socket.gethostbyname(full_domain)
        print(f"[+] Found: {full_domain} -> {ip}")
        return full_domain, ip
    except socket.gaierror:
        return None

def load_wordlist(file_path):  #verifies that fille exist <wordlist>
    """Loads subdomains from a wordlist file."""
    if not os.path.exists(file_path):
        print(f"Error: Wordlist file '{file_path}' not found.")
        sys.exit(1)
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    """Main function to handle input and subdomain enumeration."""
    if len(sys.argv) != 3:
        print("Usage: python3 subdomain-tool.py <domain> <wordlist>")
        sys.exit(1)
    
    domain = sys.argv[1]
    wordlist_path = sys.argv[2]

    # Load subdomains from wordlist
    subdomains = load_wordlist(wordlist_path)

    # Use a thread pool for concurrent subdomain resolution
    print(f"[*] Starting subdomain enumeration on: {domain}")
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(lambda sub: resolve_subdomain(domain, sub), subdomains))

    # Save results to a file
    with open("subdomains_found.txt", "w") as f:
        for result in results:
            if result:
                f.write(f"{result[0]} -> {result[1]}\n")
    print("[*] Results saved to 'subdomains_found.txt'")

if __name__ == "__main__":
    main()

