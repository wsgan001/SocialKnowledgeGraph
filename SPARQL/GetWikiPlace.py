# coding: u8
import urllib2
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
def GetIdName(place):
    #select distinct ?label,?place where {
    #    ?place ?pre <http://dbpedia.org/resource/Tainan> . 
    #    ?place <http://www.w3.org/2003/01/geo/wgs84_pos#geometry> ?geo.
    #    ?place <http://www.w3.org/2000/01/rdf-schema#label> ?label.
    #    FILTER (lang(?label) = 'zh')
    #}
    #limit 100000
    #url = "http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=select+distinct+%3Flabel%2C%3Fplace+where+%7B%0D%0A%3Fplace+%3Fpre+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F"+place+"%3E+.+%0D%0A%3Fplace+%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23geometry%3E+%3Fgeo.%0D%0A%3Fplace+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23label%3E+%3Flabel.%0D%0AFILTER+%28lang%28%3Flabel%29+%3D+%27zh%27%29%0D%0A%7D%0D%0Alimit+100000%0D%0A&format=text%2Fhtml&CXML_redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=30000&debug=on"
    
    #===============================================================================================
    #select distinct ?place where {
    #        ?place ?pre <http://dbpedia.org/resource/Tainan> . 
    #        ?place <http://www.w3.org/2003/01/geo/wgs84_pos#geometry> ?geo.
    #        }
    #limit 100000
    url = "http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=select+distinct+%3Fplace+where+%7B%0D%0A%3Fplace+%3Fpre+%3Chttp%3A%2F%2Fdbpedia.org%2Fresource%2F"+place+"%3E+.+%0D%0A%3Fplace+%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23geometry%3E+%3Fgeo.%0D%0A%7D%0D%0Alimit+100000%0D%0A&format=text%2Fhtml&CXML_redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=30000&debug=on"

    try:
        Rset = set()
        response = urllib2.urlopen(url)
        html = response.read()
        tmp = html.split("<td><a href=\"http://dbpedia.org/resource/")
        for i in range(1,len(tmp),1):
            Rset.add(tmp[i].split("\"")[0])
        return Rset
        #print html
    except:
        pass

#Rset = set()
def traverse(place,status):
    #global Rset
    Pset = GetIdName(place)
    if len(Pset)==0:return
    for x in Pset:
        if x in status.split("\t"): #cycle
            continue
        #Rset.add(x)
        print status+"\t"+x
        traverse(x,status+"\t"+x)

traverse("Tainan","Tainan")
#print len(GetIdName("Tainan"))
