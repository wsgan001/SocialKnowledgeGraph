import sys
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    print tmp[len(tmp)-1]
