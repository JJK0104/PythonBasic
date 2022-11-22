
from selenium import webdriver
import time

# 뷰티풀수프 임포트
from bs4 import BeautifulSoup

driver = webdriver.Chrome('D:/py1530/chromedriver.exe')
driver.get('https://www.aladin.co.kr')

driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

# 페이지 로딩 시간을 고려하여 코드실행을 중단시킴
time.sleep(3)

# selenium으로 <현재 페이지>의 html소스코드 가져오기
source = driver.page_source
# print(source)

# 뷰티풀수프 객체 생성
html_s = BeautifulSoup(source, "html.parser")

'''
- 뷰티풀수프 객체를 사용하여 크롤링하고 싶은 데이터가 들어있는 태그를
  추출합니다.

- find_all()메서드는 인수값으로 추출하고 싶은 태그의 이름을 적으면
  해당 태그를 전부 추출하여 리스트에 담아 리턴합니다.
'''
best_seller_div = html_s.find_all("div", class_="ss_book_box")

# print("리스트 요소의 개수:", len(best_seller_div))

# print(best_seller_div[0])

for best_seller in best_seller_div: # best_seller_div에는 50개가 들어있다

    first_book = best_seller.find_all("li")
    # print(first_book)
    
    # 증정품이 있으면 첫 요소가 바로 제목이 나오지만 증정품이 있으면 2번째 요소부터 제목이 나온다
    if first_book[0].text[0] == "[":
        book_title = first_book[1].text
        book_author = first_book[2].text
        book_price = first_book[3].text
    else:
        book_title = first_book[0].text
        book_author = first_book[1].text
        book_price = first_book[2].text
        

    print("책 제목: " + book_title)
    print("저자: " + book_author)
    print("가격: " + book_price)
    print("-" * 50)








