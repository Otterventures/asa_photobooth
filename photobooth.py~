#!/usr/bin/env/python

import datetime
from subprocess import call

while (True):
    time = str(datetime.datetime.now())
    filename = time.replace(' ', '_') + '.jpg'
    call(['raspistill', '-f', '-fp', '-vf', '-k', '-t', '99999', '-o', filename])
#    call("raspistill -f -fp -ex auto -awb auto -vf -k -t 99999999 -o test.jpg"}
