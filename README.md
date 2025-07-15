create a subdomains.txt
follow the command >>  # Clone SecLists (if you don’t have it yet)
git clone https://github.com/danielmiessler/SecLists.git

# Use a large subdomain wordlist
cp SecLists/Discovery/DNS/subdomains-top1million-5000.txt ./subdomains.txt

clone and ready to use
>> python3 <py-file> <dns> subdoamins.txt
