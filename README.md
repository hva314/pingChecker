# pingChecker

A basic python program perfoms ping check on a given list of IP

## Installing

A singple python2 file with no prerequisites required but python itself.

## Usage

```
./pingChecker.py -h
usage: pingChecker.py [-h] [-r <RANGE>] [-f <FILE>] [-t <INTERVAL>]
                      [-w <TIMEOUT>] [-c <PACKETS>] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -r <RANGE>     IP Range
  -f <FILE>      Read list of IPs from file
  -t <INTERVAL>  Run periodically, with interval
  -w <TIMEOUT>   Ping timeout, default=2s
  -c <PACKETS>   Number of ping packet, default=1
  -v             Print all hosts

```

### Example on HackTheBox range:

```
./pingChecker.py -r 10.10.10.0/24
 [+]  Start scanning
 [+]  2019-02-06 02:13:20.191077
  10.10.10.2       UP     ttl=64    49.411ms
  10.10.10.4       UP     ttl=127   51.454ms
  10.10.10.5       UP     ttl=127   49.915ms
  10.10.10.6       UP     ttl=63    49.945ms
  10.10.10.8       UP     ttl=127   49.709ms
  10.10.10.9       UP     ttl=127   48.880ms
  10.10.10.31      UP     ttl=63    49.838ms
  10.10.10.51      UP     ttl=63    49.329ms
  10.10.10.56      UP     ttl=63    50.308ms
  10.10.10.59      UP     ttl=127   98.436ms
  10.10.10.65      UP     ttl=63    67.654ms
  10.10.10.66      UP     ttl=63    49.687ms
  10.10.10.68      UP     ttl=63    48.509ms
  10.10.10.70      UP     ttl=63    49.037ms
  10.10.10.72      UP     ttl=127   49.964ms
  10.10.10.77      UP     ttl=127   50.239ms
  10.10.10.84      UP     ttl=63    49.759ms
  10.10.10.86      UP     ttl=63    49.298ms
  10.10.10.87      UP     ttl=63    50.226ms
  10.10.10.94      UP     ttl=63    50.047ms
  10.10.10.96      UP     ttl=63    49.332ms
  10.10.10.98      UP     ttl=127   50.010ms
  10.10.10.103     UP     ttl=127   49.725ms
  10.10.10.104     UP     ttl=127   57.933ms
  10.10.10.105     UP     ttl=63    49.875ms
  10.10.10.106     UP     ttl=127   49.018ms
  10.10.10.107     UP     ttl=254   49.835ms
  10.10.10.108     UP     ttl=63    48.846ms
  10.10.10.109     UP     ttl=63    48.865ms
  10.10.10.111     UP     ttl=63    49.760ms
  10.10.10.112     UP     ttl=127   60.090ms
  10.10.10.113     UP     ttl=63    48.571ms
  10.10.10.116     UP     ttl=127   49.651ms
  10.10.10.117     UP     ttl=63    73.991ms
  10.10.10.119     UP     ttl=63    49.488ms
  10.10.10.120     UP     ttl=63    49.170ms
  10.10.10.121     UP     ttl=63    50.223ms
  10.10.10.122     UP     ttl=63    57.204ms
  10.10.10.124     UP     ttl=63    50.348ms
  10.10.10.150     UP     ttl=63    49.459ms
  10.10.10.153     UP     ttl=63    51.548ms
 [+]  2019-02-06 02:13:22.797896
 [+]  Finish scanning after  2.6069 seconds   Up host: 41/254

```
![Alt text](example.png "Example")

## Versioning

0.01

## Authors

Blue