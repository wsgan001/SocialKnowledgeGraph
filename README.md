# SocialKnowledgeGraph
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

(5) 
