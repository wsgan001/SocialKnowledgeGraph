# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
#處理編碼的套件
import operator
##處理字典檔排序的套件

f = codecs.open(sys.argv[1],"r","utf-8")
#讀取存成TXT檔的文字，讀入後統一轉成UTF-8格式

def ngram(text,n): #第一個參數放處理好的文章，第二個參數放字詞的長度單位

    words=[]     #存放擷取出來的字詞
    words_freq={}#存放字詞:計算個數 
    
    for w in range(len(text)-(n-1)): #要讀取的長度隨字詞長度改變
        try:
            words.append(text[w:w+n])    #抓取長度w-(n-1)的字串
            words.append(text[w:w+n+1])
            words.append(text[w:w+n+2])
            words.append(text[w:w+n+3])
        except:continue
    return words


f2 = codecs.open(sys.argv[2],"r","utf-8")
Edict = dict()
while True:
    line = f2.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    try:
        Edict[tmp[0]] = tmp[1]
    except Exception as e: print str(e)
    #except:
    #    pass

while True:
    line = f.readline()
    if not line:break
    if line=="===============================================":
        IdName = f.readline()
        line = f.readline()
    line = line.replace("\n","")
    tmp = line.split("\t")
    try:
        Wlist = ngram(tmp[2],2)
        for x in Wlist:
            if x in Edict.keys():
                print tmp[0]+"\t"+tmp[1]+"\t"+x
        
        #break
    except : pass
    #except Exception as e: print str(e)

