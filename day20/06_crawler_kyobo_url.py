'''
교보문고 베스트셀러 상세 정보, 제목 눌렀을 때 들어가지는 페이지 URL 주소를 크롤링 할 거다 
'''


from selenium import webdriver
import time
from bs4 import BeautifulSoup
import codecs
from datetime import datetime

d = datetime.today()

file_path = "C:/py1530/교보문고 베스트셀러URL_%d_%d_%d.txt" % (d.year, d.month, d.day)

try:
    f = codecs.open(file_path, mode="w", encoding="utf-8")
except:
    print("디렉토리 경로를 찾을 수 없습니다.")

driver = webdriver.Chrome('C:/py1530/chromedriver.exe')
# 교보문고 베스트셀러 주소로 바로 가기
driver.get('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79')

'''
책 상세페이지 링크 페이지 URL 주소가 궁금하다
그 data가 어디 있길래 우리가 클릭했을 때 그 주소로 향하는가
HTML 소스코드 안에 있다

F12 누르고 왼쪽 상단 박스안 마우스 아이콘 클릭해서
책 제목 눌러보면 소스코드가 잡히는데 소스코드 위에 뭔가 웹주소가 적혀있다
혹시 이 주소가 이 1위책에 대한 상세정보 페이지일까? 한번 눌러본다
맞다. 
이제 저기에 가까워지려면 .find_all을 할건데 이 때 우리는 div 태그 찾아라, class 이름이나 id 이름 확인해라
운 좋게 바로 <div class="title"> 이 보인다

혹시 모르니 체크 해보자
F12 누르고 왼쪽 상단 박스안 마우스 아이콘 눌러서 제목을 포함하고 있는 div가 잡히는 영역으로 가보자
div.title이라 뜬다

그럼 이 페이지에 베스트셀러 1위~20위 까지 있으니 div.title이 총 20개 있을거다
확인해보면 페이지에서 우클릭 - 페이지 소스 보기 클릭
Ctrl+f 누르고 <div class="title" 검색해보자
근데 20개가 아니라 36개가 뜬다

36개를 찾아보니 처음 16개는 서비스, 90년대 베스트, 등등 우리가 원하는 정보가 아니고
뒤에 20개만 책정보다
'''

time.sleep(2)
# 이 페이지의 소스코드를 갖고 오기
src = driver.page_source
# 뷰티풀수프 객체 생성
html_s = BeautifulSoup(src, "html.parser")

# div title 전부 데리고 오기
title_list = html_s.find_all("div", class_="title")
print()
print(len(title_list))  # 52개가 뜨네...
print()
print(title_list)
# 이부분에 뜨는 거 복사해서 메모장에 붙여놓고 확인해보니 마지막 33번부터 52번까지가 책정보 
# ctrl+f 로 div 찾아서 나누면 편함
print()
for i in range(32,52):
    print("%d위 :"  % (i-31) + title_list[i].text.strip() ) # 여기서 i-31에 괄호 안 씌워주면 오류뜬다
print()

'''
메모장에 복붙해놓은 걸 다시 살펴보면 
우리가 찾는 주소는 a 태그에 있다

* 참고로 태그 이름은 < 바로 뒤에 나오는 거다
<div -> div 태그
<a -> a 태그
<span -> span 태그
<img -> img 태그

그래서 이제 a 태그를 다시한번 find
url = title_list[32].find_all("a")

한개밖에 없는 게 확실하다면 find_all 대신 그냥 find만 써도 된다
url = title_list[32].find("a")
print(url) 하면 아래처럼 뜨는데

<a href="http://www.kyobobook.co.kr/product/detailViewKor.laf?
mallGb=KOR&amp;ejkGb=KOR&amp;barcode=9791165343729" onclick="javascript:ecommerceClickListGA('9791165343729', 'KOR', 
'달러구트 꿈 백화점. 2', '팩토리나인', '010108', '이미예', '');"><strong>달러구트 꿈 백화점. 2</strong></a>

text면 그냥 .text하면 되는데 태그는 다른 명령어 없다
이 상태에서 우리가 이제 직접 문자열 조작을 통해 정제해야한다

위 문자열을 " ("공백)으로 split하면 2개로 쪼개지고 0번 인덱스 취하면
<a href="http://www.kyobobook.co.kr/product/detailViewKor.laf?
mallGb=KOR&amp;ejkGb=KOR&amp;barcode=9791165343729 
가 나오고

여기서 또 "뒤로만 슬레이싱 해주면
http://www.kyobobook.co.kr/product/detailViewKor.laf?
mallGb=KOR&amp;ejkGb=KOR&amp;barcode=9791165343729 
가 나온다

'''
url = title_list[32].find("a")
# print(url)
print(type(url)) # <class 'bs4.element.Tag'>
url = str(url)

print(url.split('" ')[0])
print(url.split('" ')[0][9:])

'''
print(url.split('" ')[0][9:]) 하면 아래와 같은 주소가 남는다

http://www.kyobobook.co.kr/product/detailViewKor.laf?
mallGb=KOR&amp;ejkGb=KOR&amp;barcode=9791165343729

근데 이걸 복붙해서 들어가보면 안들어가진다
그래서 실제 1위책 상세 정보 주소를 살펴보면 

http://www.kyobobook.co.kr/product/detailViewKor.laf?
mallGb=KOR&ejkGb=KOR&barcode=9791165343729

이다

비교해보니 amp;amp;가 들어있다
html에서 해석하는 기호와 파이썬에서 해석하는 기호의 차이에서 오는 똥이다
이걸 제거해야된다

문자열에서 특정 단어를 찾아서 일괄적으로 교체하는 메서드 = replace
8일차

'''

rank = 0
for idx in range(len(title_list)):
    if idx > 31 :
        url = title_list[idx].find("a")
        url = str(url)
        # 문자열에서 특정 단어를 찾아서 일괄적으로 교체하는 메서드 = replace
        # 8일차
        rank += 1
        f.write("%d위" %rank +"\r\n")
        f.write(url.split('" ')[0][9:].replace("amp;", "") + "\r\n")
        f.write("-"*50 + "\r\n")

f.close()
print("URL크롤링 완료!")








