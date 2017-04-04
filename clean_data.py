from collections import Counter
import re

logfile = open('log.txt', 'r')
log_table = []
ipcount = Counter()
bandwidth = Counter()

for line in logfile:
    ip, tmp = line.split(' - - [', 1)
    time, tmp = tmp.split('] "', 1)
    tmp = re.sub('([A-Za-z]+ )', '', tmp)  # debating whether or not to keep COSTLY
    request, tmp = tmp.split('" ', 1)
    code, dsize = tmp.split(' ', 1)
    if '-' in dsize:
        dsize = ''
    else:
        dsize = dsize.strip('\n')
        bandwidth[request] += 1 + int(dsize)

    log_table.append([ip, time, request, code, dsize])
    ipcount[ip] += 1

topTenIPs = ipcount.most_common(10)
bigBand = bandwidth.most_common(10)


# populate hosts.txt

host = open('hosts.txt', 'w')

for (a,b) in topTenIPs:
    host.write(a + ',' + str(b) + '\n')

host.close()