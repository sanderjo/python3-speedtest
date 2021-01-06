#!/usr/bin/env python3

import urllib.request
import sys
import os
import time

# Download the file from `url`, save it in a temporary directory and get the
# path to it (e.g. '/tmp/tmpb48zma.txt') in the `file_name` variable:

try:
        url = sys.argv[1]
except:
        print("No URL specificied, so using default")
        url = 'http://speed.transip.nl/100mb.bin'

print("Start getting", url)
start_time = time.time()

file_name, headers = urllib.request.urlretrieve(url)

duration = time.time() - start_time
mysize = os.stat(file_name).st_size
print(file_name, mysize, duration)
speedMBs = mysize / duration / (1024*1024)
print("Speed in MB/s: {:.1f}".format(speedMBs))
os.remove(file_name)

