#!/usr/bin/env python
import os
import sys
from ipaddr import IPAddress
def parse_host(host):
    try:
        IPAddress(host)
        return host
    except ValueError:
        f=open('/etc/hosts')
        lines=f.readlines()
        f.close()
        for line in lines:
            if line[0]=='#':
                continue
            tokens=line.split()
            if len(tokens)>1 and tokens[1]==host:
                return tokens[0]
            if len(tokens)>2 and tokens[2]==host:
                return tokens[0]
def run():
    cmd='corkscrew '+" ".join(sys.argv[1:3])+" "+parse_host(sys.argv[3])+" "+" ".join(sys.argv[4:])
#    print cmd
    os.system(cmd);
if __name__=='__main__':
    run();
