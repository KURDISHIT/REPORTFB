 
import os, sys, time
P = '\x1b[0m'
H = '\x1b[91m'
G = '\x1b[92m'
K = '\x1b[93m'

def Loads():
    for i in range(101):
        time.sleep(0.3)
        sys.stdout.write(G + '\r[+] ' + P + 'CHAWAREKA : %d%%' % i)
        sys.stdout.flush()


def Report():
    for d in range(101):
        time.sleep(0.2)
        sys.stdout.write(G + '\r[*] ' + P + 'Mulai Processing ... [%d%%] ' % d)
        sys.stdout.flush()
print '-' * 49 + H
os.system('figlet " R E P O R T FB"')








print '\x1b[96mTelegram ==> Dragon_Crack4'
print '\x1b[96mYou tube Chanell==> Miran Boss'
print '\x1b[92mTelegram Chnell ==> KURDISH IT'
print '\x1b[92mTEBENI ==> LA 1000 REPORT ASWTET'
print P + '=' * 49
B = raw_input(G + '[+]' + P + ' ID TARGET  : ')
print '=' * 49
if not B.startswith('1000'):
    print '[!] Id rastneya'
    sys.exit()
    print '=' * 49
Loads()
time.sleep(3)
print ''
print '=' * 49
a = 1
while True:
    print ('{}[-] {}Chawarwanba ta tawawdbet [{}] => {}{}').format(G, P, a, H, B)
    print ('{} | {}[+]{} Report Roysht').format(Report(), K, G)
    print '=' * 49
    a += 1
