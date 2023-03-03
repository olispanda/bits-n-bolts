#!/bin/sh
# launcher.sh

cd /home/oliver/bits-n-bolts
sleep 60
echo "Hello"
# # clear > /dev/tty1
python3 main.py >> applog.log 2&>1

