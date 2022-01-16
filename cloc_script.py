import sys
import wget
import subprocess
from send_email import sendEmail

# retrieve github repo zip file link from first command line argument
url = sys.argv[1]

# download repo zip file
filename = wget.download(url)
print(chr(10))
print('GitHub repository zip file downloaded.\n')

# create out.txt file, scan repo zip file with cloc, and store scan results to out.txt file
with open('out.txt', 'w') as out:
    print('Scanning zip file to count lines of code.\n')
    results = subprocess.run(
        ["cloc", f"{filename}"], stdout=out, stderr=subprocess.PIPE, text=True)
    print('Scan completed.\n')

# email scan results
with open('out.txt', 'r') as f:
    sendEmail(f.read())
