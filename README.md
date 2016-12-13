# 抓出台南相關的facebook頁面
(0) 一開始擁有9000個粉絲團ID ： 
<br>IdList.txt

(1) 取得粉絲團ID對應name
<br>$ python GetIdName.py IdList.txt > IdName.txt

(2) 抓出IdName.txt中, 有台南的部份
<br>$ grep "台南" IdName.txt > TainanFromIdName.txt

(3) 使用facebook graph api search 找出台南相關的粉絲團
<br> $ python GetTainanPage.py > TainanPage.txt

(4) 將上述兩種方式取得的台南粉絲團合併
<br> TainanMerge.txt

# 使用graph api抓出粉絲團PO文, comment等資訊
(1) 抓某個頁面的Po文以及comment到local的json檔
<br> ?fields=name,feed{message,created_time,id,comments}
<br> $ python GetJsonPage.py > JsonPage.txt

(2) 讀取Json
<br> $ python ParseJsonPage.py JsonPage.txt
<br> // 目前只有印到螢幕, 未來要寫入DB

# 使用SPARQL抓出DBpedia中地點的page
(1) 抓出DBpedia中台南的所有地點 (有階層性)
<br> $ python GetWikiPlace.py > WikiTainanPlace.txt
