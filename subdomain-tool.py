#!/bin/python3
'''
import requests  # To send HTTP requests
import sys       # For command-line arguments
import concurrent.futures  # For parallel processing to speed up subdoamin checking

def check_subdomain(subdomain): #defining the check_subdomain function
    """
    Function to check if a subdomain is live.
    """
    url = f"http://{subdomain}"  # Construct the full URL
    try:
        response = requests.get(url, timeout=3)  # Send HTTP GET request with a 3-second timeout
        if response.status_code == 200:  # Check if the subdomain is live, if response is 200
            print(f"[+] Live Subdomain Found: {url}")
            return url  # Return the live subdomain
    except requests.RequestException:
        pass  # Ignore any errors like timeouts or connection errors
    return None  # Return None if the subdomain is not live

def main():
    """
    Main function to read subdomains and test them.
    """
    if len(sys.argv) < 3:  #ensures user provides appropriate arguments
        print("Usage: python subdomain_enum.py <domain> <wordlist>")
        sys.exit(1)  # Exit if incorrect usage

    domain = sys.argv[1]  # First argument: Target domain
    wordlist_file = sys.argv[2]  # Second argument: Subdomain wordlist file

    # Read the wordlist
    try:
        with open(wordlist_file, 'r') as file:
            subdomains = file.read().splitlines()  # Read each line as a subdomain
    except FileNotFoundError:
        print(f"Wordlist file '{wordlist_file}' not found.")
        sys.exit(1)

    # Generate full subdomain URLs
    full_subdomains = [f"{sub}.{domain}" for sub in subdomains]

    # Check subdomains in parallel
    print("[*] Checking subdomains...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_subdomain, full_subdomains)

    # Save results
    live_subdomains = [result for result in results if result]
    if live_subdomains:
        with open("live_subdomains.txt", "w") as file:
            file.write("\n".join(live_subdomains))
        print(f"[+] Results saved to 'live_subdomains.txt'")
    else:
        print("[-] No live subdomains found.")

if __name__ == "__main__":
    main()
the complexities are
DNS  resolution
Concurrency: process subdomains sequentially 
output : reuslts are printed but saved to a file for futher use
 

create another file containing as wordlist.txt and include
www
mail
admin
test
api
'''
