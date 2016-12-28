import sys
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    try:
        if "feed" not in line:
            print line.split("\"id\":\"")[1].split("\"")[0]
    except:pass
