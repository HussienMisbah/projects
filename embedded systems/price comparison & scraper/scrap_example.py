import requests
from bs4 import BeautifulSoup

name = "samsung galaxy s8"
name1 = name.replace(" ","+")
global ebay
url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0"
res = requests.get(url)

print(res.text) # comment this 

# uncomment this to get BeautifulSoup output 
# bs = BeautifulSoup(res.text,"html.parser")
# for i in range(1,len(bs.select('.s-item__title')) ) :
#     ebay_name = bs.select('.s-item__title')[i].getText().strip()
#     print(ebay_name)
