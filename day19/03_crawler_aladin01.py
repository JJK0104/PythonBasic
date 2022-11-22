# 사이트가 업데이트 되거나 바뀌면 아래 주소, 리스트 내 요소 순서, 개수 변화 생김

from selenium import webdriver
import time

# 뷰티풀수프 임포트
from bs4 import BeautifulSoup

driver = webdriver.Chrome('D:/py1530/chromedriver.exe') # webdriver 모듈에 있는 클래스 Chrome을 호출, Chrome의 객체를 생성.
driver.get('https://www.aladin.co.kr') # 알라딘 간다

# 베스트셀러 란 클릭 
driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

# 페이지 로딩 시간을 고려하여 코드실행을 중단시킴
time.sleep(3)

'''
우리가 할 건 알라딘 베스트셀러 top50 or top 400 등 일정 범위 내 
책 제목, 출판사, 가격, 출판일을 뽑아내는 거 

1) 그럼 일단 우클릭 - 페이지 소스 보기 클릭
2) 코드가 5000줄이 넘는다, 한번 ctrl+f 눌러서 베스트셀러 1위 제목 검색
그럼 해당 책의 정보가 있는 줄을 쉽게 찾을 수 있다

크롤링의 시작은 selenium으로 우리가 원하는 장소에 자동으로 접근한 다음에 거기 있는 data를 전부 끌고 오는게 목적이다
일단 5,000줄 다 끌고 와 그러면 BeautifulSoup 가지고 자를 건 자르면서 우리가 원하는 data로 정제시킴

'''

# selenium으로 <현재 페이지>의 html소스코드 가져오기
source = driver.page_source # 크롬객체 driver, driver self변수 중에(멤버변수 중에) page_source라는 변수가 있다
# 이걸 source라는 변수에 저장

# print(source) 한번 확인해봐


'''
알라딘에서 베스트셀러에서 f12 누르고 Xpath 찾을 때 눌렀던 박스안 마우스 모양 누르고 
1위책의 지은이, 출판사, 출판일 ,가격 등을 전부 커버하는 영역을 찾는다
마우스를 미세하게 컨트롤 하면서 찾으면 아마 가장 먼저 말풍선에 td라고 적혀 있는게 찾아질 거다
아쉽지만 그건 찾는 게 아니다, 우리가 찾는 건 div이다
마우스를 미세하게 내리다 1위 책과 2위 책 빈공간에 갖다 대면 말풍선에 div.ss_book_box라고 뜬다
div. 의 .은 class를 의미한다, 어떤 사이트는 .이라 안 나오고 # 이라 나오는데 #은 id의미다

div.ss_book_box 를 html 코드로 표현하면 <div class = "ss_book_box">
div#apple 은 <div id="apple">

자 그러면 ss_book_box라는 클래스 이름을 가진 div 영역에 우리가 원하는 텍스트 데이터가 모여있다
그럼 5000줄 코드 중 저거만 추출하면 된다

2위책, 3위책 ... 모두 div.ss_book_box이다
대부분의 사이트가 비슷한 모양의 division에는 class 이름이 똑같다. 반복문 돌렸을테니

그러면 우리는 class 이름이 ss_book_box인 div 태그에 접근하면 1위~몇위까지든 텍스트 data를 반복문으로
갖고 올 수 있다

지금 한 페이지에 책이 50개 있으니 페이지 소스 보기에서 Ctrl+f 누르고 <div class ="ss_book_box 라고 
검색하면 50개 뜬다

'''

# 뷰티풀수프 객체 생성
html_s = BeautifulSoup(source, "html.parser") # BeautifulSoup는 init에 처음에는 html소스코드 주고
# 두번째 인수는 "html.parser" 라고 적는다
# driver.page_source가 들고오는 소스코드가 text 형태다, 문자열 형태기 때문에 BeautifulSoup가 작업 하려면 태그를 이해해야 되는데 
# 태그를 이해할 수 있도록 다시 html 형태로 구조를 바꿔주는 역할

'''
- 뷰티풀수프 객체를 사용하여 크롤링하고 싶은 데이터가 들어있는 태그를
  추출합니다.

- find_all()메서드는 인수값으로 추출하고 싶은 태그의 이름을 적으면
  해당 태그를 전부 추출하여 <리스트>에 담아 리턴합니다.

- find_all()이 데리고 올 때는 제일 위에 검색되는 애부터 0번 인덱스에 담는다
'''
best_seller_div = html_s.find_all("div", class_="ss_book_box") # 인자값으로 추출하고 싶은 태그 이름 "div" 적는다. 
# 만약 그중에서도 class 이름이 "ss_book_box"인 애들을 추출하고 싶으면 2번째 인수로 class_ = "ss_book_box"라고 적는다 
# class는 키워드라 인수로 사용할 수 없어서 class_로 지었다
# 만약 다른 사이트에서 id가 "banana" 이면 2번째 인수로 id = "banana"라고 적으면 된다

# print("리스트 요소의 개수:", len(best_seller_div))

# print(best_seller_div[0])
# find_all()이 데리고 올 때는 제일 위에 검색되는 애부터 0번 인덱스에 담는다
# 따라서 0번인덱스에는 1위책에 대한 정보가 담겨 있고 .... 49번 인덱스에는 50위책에 대한 정보가 있다

# 근데 우리가 필요한 책제목, 작가,출판사,출판일,가격 이외에도 아직 정보가 많다
# 다시 f12눌러서 박스안 마우스 아이콘 눌러서 우리가 필요한 정보에 갖다 대보면 
# 태그 이름이 li 라는 걸 확인할 수 있다
print("\n\n")
print(best_seller_div)
print(type(best_seller_div)) # <class 'bs4.element.ResultSet'>
print(type(best_seller_div[0])) # <class 'bs4.element.Tag'>
print("\n\n")

first_book = best_seller_div[0].find_all("li") # 1위책 div에서 li들을 전부 추출해서 first_book이라는 변수에 저장
# print(first_book) -> 이거 복사해서 메모장에다 붙여넣고 ctrl+f 로 li 찾아서 한줄씩 나눠보면 요소가 8개 나온다
# 이 중 2 번째 요소에 책제목, 3번째 요소에 작가, 출판사, 출판일, 4번째 요소에 가격이 있다


'''
html은 태그와 태그가 아닌 text로 코드가 구성된다
태그와 text를 어떻게 구분하느냐
<div> 
  <li> <a href="hello.com">
  <b> 안녕하세요!</b></a><li>

</div>  
<> 안에 들어있으면 태그다
위 코드에서 hello.com은 태그지만 
안녕하세요!는 text다
'''
# 첫번째 책은 2 번째 요소에 책제목, 3번째 요소에 작가, 출판사, 출판일, 4번째 요소에 가격이 있다
book_title = first_book[1].text # .text는 text만 추출
book_author = first_book[2].text
book_price = first_book[3].text

print()
print()
print("책 제목: " + book_title)
print("저자: " + book_author)
print("가격: " + book_price)

# 이제 문자열 관리 메서드를 통해서 예쁘게 조작하면 된다
# N위 까지의 책을 반복문을 돌려서 추출한 다음에 파일 입출력으로 세이브하면 된다

# w3schools.com 에 들어가면 html, css , 자바스크립, 자바, 파이썬 등 무료로 배울 수 있다.




