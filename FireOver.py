import argparse
import re
import sys
from util.takeover import Takeover
from util.delete import deletepoc
from util.banner import banner

try:
    from printy import printy,inputy
except:
    print(banner)
    print("Requirements Error ,Please install requirements from requirements.txt")
    sys.exit()
printy(banner,predefined='n')


parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',help="Firebase Database URL",dest='url')
parser.add_argument('-l','--list',help="Location of File having list of URL\'s",dest='list')
parser.add_argument('-o','--output',help="Location of Output file",dest='out')
parser.add_argument('-d','--delete',help="Enter POC file location to delete all pocs\'s",dest='delete')
args=parser.parse_args()
url=args.url
ifile=args.list
out=args.out
delete=args.delete
if not out:
    out='poc.txt'

if args.url:
    Takeover(url)
    sys.exit()
elif args.list:
    urls=[]
    urls=open(ifile).read().splitlines()
    f=open(out,'w+')
    for url in urls:
        temp=Takeover(url)
        f.write(temp+'\n')
    f.close()
    printy("\n\n[*]POC URLS file stored at:\t" + out,'y>')
    sys.exit()
elif delete:
    urls=[]
    urls=open(delete).read().splitlines()
    for url in urls:
        deletepoc(url)
    sys.exit()
else:
    printy("Invalid arguments or Unknown Errors Please Submit the issue","r>")
