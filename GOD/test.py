import sys
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    if "--" in tmp[2] or "." in tmp[2] or len(tmp[2])<6:continue
    print line
