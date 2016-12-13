import sys
import json
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    J = json.loads(line)
    print J['id']+"\t"+J['name']
    print J['feed']['data'][0]['id']
    print J['feed']['data'][0]['comments']['data'][0]['message']

    #for i in range(len(J['feed']['data'])):
    #    print J['feed']['data'][i]['message'].encode('utf-8')
    #    print "============================================"

