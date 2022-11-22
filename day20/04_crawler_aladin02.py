
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import codecs
from datetime import datetime

d = datetime.today()

file_path = "C:/py1530/알라딘 베스트셀러_%d_%d_%d.txt" % (d.year, d.month, d.day)

'''
우리가 기존에 배운 파일 입출력은 내부에서 data를 만들어서 내부에 있는 data를 파일에 저장시킴
근데 이번에는 외부에서 가져온 data이다
웹의 인코딩 방식과 파이썬 내부의 인코딩 방식의 차이 때문에 
파이썬 코덱이 웹에 있는 data를 밖에 파일로 내보내는 과정에서 인코딩 문제가 생김
내장함수 open 같은 경우에는 이 인코딩 문제를 해결할 수 있는 방법이 없다

파이썬의 표준모듈, 내장 설치된 모듈 중에 codecs라는 모듈이 있는데 우리는 codecs라는 모듈을 통해서 
파일을 writing 할 때, 파일을 save 할 때 인코딩 방식을 바꿔줄 수 있다 
'''
try:
    f = codecs.open(file_path, mode="w", encoding="utf-8")
except:
    print("디렉토리 경로를 찾을 수 없습니다.")

driver = webdriver.Chrome('C:/py1530/chromedriver.exe')
driver.get('https://www.aladin.co.kr')

driver.find_element_by_xpath('//*[@id="re_mallmenu"]/ul/li[3]/div/a/img').click()

time.sleep(3)
source = driver.page_source
html_s = BeautifulSoup(source, "html.parser")

best_seller_div = html_s.find_all("div", class_="ss_book_box")

rank = 1
for best_seller in best_seller_div:

    first_book = best_seller.find_all("li")    
    
    if first_book[0].text[0] == "[":
        book_title = first_book[1].text
        book_author = first_book[2].text
        book_price = first_book[3].text
    else:
        book_title = first_book[0].text
        book_author = first_book[1].text
        book_price = first_book[2].text
    
    info = book_author.split("|")
    # codecs.open write 할때 줄바꿈할때 \n만 쓰면 안되고 
    # 사실 enter 키는 \r\n 같이 들어감
    f.write("순위: %d위\r\n" % rank)
    f.write("책 제목: " + book_title + "\r\n")
    f.write("저자: " + info[0].strip() + "\r\n") # strip으로 공백 제거 
    f.write("출판사: " + info[1].strip() + "\r\n")
    f.write("출판일: " + info[2].strip() + "\r\n")
    f.write("가격: " + book_price.split(",  ")[0] + "\r\n") # 그냥 ","으로 split하면 13,800 같은 숫자도 나눠지는데 다행히도 마일리지 앞에
    # , 마일리지 형태로 적혀 있으니 ", "로 split
    f.write("-" * 50 + "\r\n")
    rank += 1

f.close()
print()
print()
print("크롤링 완료!")






