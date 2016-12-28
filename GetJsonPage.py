# coding: u8
import urllib2
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
def GetIdName(PID):
    # ?fields=name,feed{message,created_time,id,comments}
    url = "https://graph.facebook.com/v2.8/"+PID+"?fields=name%2Cfeed%7Bmessage%2Ccreated_time%2Cid%2Ccomments%7D&access_token=1037130463075804|JDrzBrT83w5VMj1uEHyBWPFZmWw"

    # ?fields=name,feed{message,created_time,id}&limit=1000
    #url = "https://graph.facebook.com/v2.8/454836154602708?fields=name%2Cfeed%7Bmessage%2Ccreated_time%2Cid%7D&limit=1000&access_token=1037130463075804|JDrzBrT83w5VMj1uEHyBWPFZmWw"

    try:
        response = urllib2.urlopen(url)
        html = response.read()
        print html
        ###J = json.loads(html)
        ###print J['id']+"\t"+J['name']
        ###print J['feed']['data'][0]['id']
        ###print J['feed']['data'][0]['comments']['data'][0]['message']
        #for i in range(len(J['data'])):
        #    print J['data'][i]['id']+"\t"+J['data'][i]['name']
    except:
        print "ERROR"
        pass

#GetIdName("454836154602708")
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    tmp = line.split(" ")
    print tmp[0],
    GetIdName(tmp[0])
