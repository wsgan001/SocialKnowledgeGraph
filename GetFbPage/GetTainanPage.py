# coding: u8
import urllib2
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
def GetIdName(query):
    #url = "https://graph.facebook.com/v2.8/search?q=%E5%8F%B0%E5%8D%97&type=page&access_token=EAAYB7Omr1uYBANKFoSnHlIy7ZC1V0WADA1cepdyqomniGOTY4N3Kt8stPfheQCZBsmxn54zwf25VZCs3CPlvDelndY0Y6mETHgApdhoAb3IV7mdZAUQlLKBzS0xlopTlZC96O3YEfcc3vlD1AZCLOkMZBV9KMHgp7dC5d4mZBrKB8gZDZD&limit=1000https://graph.facebook.com/v2.8/search?q=%E5%8F%B0%E5%8D%97&type=page&access_token=EAAYB7Omr1uYBANKFoSnHlIy7ZC1V0WADA1cepdyqomniGOTY4N3Kt8stPfheQCZBsmxn54zwf25VZCs3CPlvDelndY0Y6mETHgApdhoAb3IV7mdZAUQlLKBzS0xlopTlZC96O3YEfcc3vlD1AZCLOkMZBV9KMHgp7dC5d4mZBrKB8gZDZD&limit=1000"
    #url = "https://graph.facebook.com/v2.8/search?q=%E5%8F%B0%E5%8D%97&limit=100000&type=page&access_token=1037130463075804|JDrzBrT83w5VMj1uEHyBWPFZmWw"
    url = "https://graph.facebook.com/v2.8/search?q="+query+"&limit=100000&type=page&access_token=1037130463075804|JDrzBrT83w5VMj1uEHyBWPFZmWw"
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        #print html
        J = json.loads(html)
        for i in range(len(J['data'])):
            print J['data'][i]['id']+"\t"+J['data'][i]['name']
    except:
        pass

GetIdName("台南")

f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    try:
        GetIdName(tmp[1])
    except:
        pass
