# import requests
# from bs4 import BeautifulSoup

# url = "https://comic.naver.com/webtoon/weekday.nhn"
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# #print(soup.title)
# #print(soup.title.get_text())
# #print(soup.a) # soup 객체에서 처음 발견되는 a element 반환
# #print(soup.a.attrs) a element의 속성 정보를 출력
# #print(soup.a["href"]) #a element의 href 정보 출력

# #print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# #print(soup.find(attrs={"class":"Nbtn_upload"}))
# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)1
 
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) # soup 객체에서 처음 발견되는 a element 반환
print(soup.a.attrs) a element의 속성 정보를 출력
print(soup.a["href"]) #a element의 href 정보 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"}))
print(soup.find(attrs={"class":"Nbtn_upload"}))
print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)1