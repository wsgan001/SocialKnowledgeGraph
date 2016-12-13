# coding: u8
import urllib2
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
def GetIdName(GID):
    url = "https://graph.facebook.com/v2.8/"+GID+"?access_token=1690966904526566%7C1WImB8zgtmGmDIf5T0aAFjc4DXA"
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        J = json.loads(html)
        print GID+"\t"+J['name']
    except:
        pass

f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line: break
    line = line.replace("\n","")
    GetIdName(line)
