# coding: u8
import urllib2
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
def GetIdName():
    url = "https://graph.facebook.com/v2.8/search?q=%E6%96%B0%E8%81%9E&type=page&limit=1000&access_token=1037130463075804|JDrzBrT83w5VMj1uEHyBWPFZmWw"
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        #print html
        J = json.loads(html)
        for i in range(len(J['data'])):
            print J['data'][i]['id']+"\t"+J['data'][i]['name']
    except:
        pass

GetIdName()
