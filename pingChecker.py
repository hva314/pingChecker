#!/usr/bin/env python
# Author: Blue
# Scipt if written for educational purposes

import sys, struct, socket  # calculating subnet
import subprocess           # ping
import threading            # multi threading
import datetime, time       # timing
import argparse             # parsing arguments
import re                   # regex from ping output

GRN = '\033[92m'
RED = '\033[91m'
RES = '\033[0m'

parser = argparse.ArgumentParser()
parser.add_argument("-r", dest="range", 
                    help="IP Range", metavar="<RANGE>")
parser.add_argument("-f", dest="ip_file",
                    help="Read list of IPs from file", metavar="<FILE>")
parser.add_argument("-t", dest="interval",
                    help="Run periodically, with interval", metavar="<INTERVAL>")
parser.add_argument("-w", dest="timeout",
                    help="Ping timeout, default=2s", metavar="<TIMEOUT>")
parser.add_argument("-c", dest="number",
                    help="Number of ping packet, default=1", metavar="<PACKETS>")
parser.add_argument("-v", action="store_true", dest="verbose", 
                    default=False, help="Print all hosts")

args = parser.parse_args()
if len(sys.argv) < 2:
    parser.print_usage()
    sys.exit(1)

if args.timeout: TIMEOUT=args.timeout
else: TIMEOUT='2'

if args.number: NUMBER=args.number
else: NUMBER='1'

# convert subnet to list of ip
def convert_range(ranges, ip_subnet):

    if '/' in ip_subnet:
        (ip, cidr) = ip_subnet.split('/')

        bits = 32 - int(cidr) 
        start = (struct.unpack('>I', socket.inet_aton(ip))[0] >> bits) << bits 
        end = start | ((1 << bits) - 1)
        
        for i in range(start+1, end):
            ranges.append(str(socket.inet_ntoa(struct.pack('>I',i))))
        return 0

    elif '-' in ip_subnet:
        pre = ".".join(ip_subnet.split('-')[0].split('.')[:-1]) + "." 
        start = int(ip_subnet.split('-')[0].split('.')[-1])
        end = int(ip_subnet.split('-')[1])
        for i in range(start, end+1):
            ranges.append(pre+str(i))
        return 0
    return 1

# import ip from file
def import_ip(ranges, filename):
    with open(filename,'r') as f:
        for line in f:
            ranges.append(line.lstrip().rstrip())

def ping(index,ip,status):
    # this script use system 'ping' command
    out = subprocess.Popen(['ping','-c',NUMBER,'-w',TIMEOUT,ip], 
               stdout=subprocess.PIPE, 
               stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    ret = out.returncode
    m1 = re.match( r'.*(ttl=.*?) ', stdout, re.M|re.I|re.S)
    m2 = re.match( r'.*mdev = .*/(.*)/', stdout, re.M|re.I|re.S)
    
    ttl  = ""
    time = ""

    if m1: ttl = str(m1.group(1))
    if m2: time = str(m2.group(1))

    # determine status by return code
    if ret == 0:
        stat = GRN + "UP" + RES 
        stat += " "*5 + str(ttl)
        stat += " "*(10 - len(str(ttl))) + str(time) + "ms"
    else:
        stat = RED + "DOWN" + RES
    status[index] = stat

ranges  = []    # list of ips
threads = []    # threading slot
status  = []    # status for output

# getting list of ips from argument
if args.range:
    try:
        if convert_range(ranges, args.range) != 0:
            raise
    except:
        print RED, "[ERROR]", RES, "Invalid range:", args.range
        exit(1)

# getting list of ip from file
if args.ip_file:
    import_ip(ranges,args.ip_file)

if len(ranges) == 0:
    print "No HOST supplied."
    exit(1)

for i in range(len(ranges)):
    threads.append(None)
    status.append(None)

# start
while True:

    total   = len(ranges)
    up      = total

    # set timer
    start_time = datetime.datetime.now()
    start_timer = time.time()

    if not args.interval:
        print GRN ,"[+]", RES, "Start scanning"
        print GRN ,"[+]", RES, start_time

    for index in range(len(ranges)):
        ip = ranges[index]
        threads[index] = threading.Thread(target=ping, args=(index,ip,status,))
        threads[index].start()
        #time.sleep(0.1)

    # join all thread
    for i in range(len(threads)):
        threads[i].join()

    # print 
    for i in range(len(ranges)):
        if "DOWN" in status[i]:
            up -= 1
            if args.verbose == False:
                continue

        print "  %-16s %s" % (ranges[i], status[i])

    # set timer and calculate time
    end_time = datetime.datetime.now() 
    end_timer = time.time()
    total_time =  round(end_timer - start_timer,4)

    print GRN ,"[+]", RES, end_time
    print GRN ,"[+]", RES, "Finish scanning after",
    print GRN, total_time, "seconds", RES,
    print " Up host: " + GRN + str(up) + "/" + str(total) + RES

    if args.interval:
        print "Sleeping..."
        time.sleep(float(args.interval))
    else:
        break
