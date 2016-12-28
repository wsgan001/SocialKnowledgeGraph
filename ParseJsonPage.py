import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split(" ")
    line = line.replace(tmp[0]+" ","")
    try:
        J = json.loads(line)
        IdName = J['id']+"\t"+J['name']
        Mlist = J['feed']['data']
        print "==============================================="
        print IdName
        for i in range(len(Mlist)):
            Message = J['feed']['data'][i]['message']
            print J['feed']['data'][i]['id']+"\t"+J['feed']['data'][i]['created_time']+"\t"+Message.replace("\n"," ")
        ###Message = J['feed']['data'][0]['message']
        ###print J['id']+"\t"+J['name']
        ###print J['feed']['data'][0]['message']
        #print J['feed']['data'][0]['id']
        #print J['feed']['data'][0]['comments']['data'][0]['message']
    except Exception as e: 
        pass
        ###print str(e)

