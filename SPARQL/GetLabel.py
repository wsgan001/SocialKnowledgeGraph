import sys
import urllib2

def GetLabel(entity):
    url = "http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=select+distinct+%3Flabel+where+%7B%0D%0A%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F"+entity+"%3E+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23label%3E+%3Flabel%0D%0A+FILTER+%28lang%28%3Flabel%29+%3D+%27zh%27%29%0D%0A%7D+LIMIT+100&format=text%2Fhtml&CXML_redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=30000&debug=on"
    response = urllib2.urlopen(url)
    html = response.read()
    if "@zh" not in html:
        return "ERROR"
    try:
        tmp = html.split("\"@zh")[0].split("\"")
        return tmp[len(tmp)-1]
    except:
        return "ERROR"


f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    Label = GetLabel(tmp[len(tmp)-1])
    if Label != "ERROR":
        print tmp[len(tmp)-1]+"\t"+Label
