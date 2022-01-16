import sys
import wget

# retrieve github repo zip file link from first command line argument
url = sys.argv[1]

# download repo zip file
filename = wget.download(url)
print(chr(10))
print('GitHub repository zip file downloaded.\n')
