# python3-speedtest
A speedtest written in python3

# Example usages

Default usage, on Linux
```
$ ./get_file_and_report_speed.py
No URL specificied, so using default
Start getting http://speed.transip.nl/100mb.bin
/tmp/tmpaq6nhzd_ 104857600 2.1773343086242676
Speed in MB/s: 45.9
```
With a big file (3.2GB):
```
$ ./get_file_and_report_speed.py http://cdimage.ubuntu.com/daily-live/current/hirsute-desktop-amd64.iso
Start getting http://cdimage.ubuntu.com/daily-live/current/hirsute-desktop-amd64.iso
/tmp/tmp5kzhj7he 3226488832 71.03246116638184
Speed in MB/s: 43.3
```


On an old Synology Diskstation, with a fast ethernet interface (=100 Mbps = 10 MB/s):
```
$ /volume1/@appstore/sabnzbd/env/bin/python3 get_file_and_report_speed.py
No URL specificied, so using default
Start getting http://speed.transip.nl/100mb.bin
/tmp/tmplx9ewb36 104857600 10.295416116714478
Speed in MB/s: 10
```

