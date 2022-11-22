
# 인터넷에 있는 방대한 자료를 수집하는 게 목적이기 때문에 
# 인터넷을 사람이 서핑하듯이 자동화시키게 도와주는게 selenium
# 클릭을 제어하거나 로그인 창에 아이디를 입력하는 걸 자동으로 처리해줌

# beautifulsoup : selenium이 특정 data를 수집해 오면 그 data를 예쁘게 가공하는 기능을 제공하는 라이브러리


# selenium 대신 request를 쓰기도 하는데 요즘은 selenium을 많이 사용해서 selenium 추천
# 책 살때도 selenium 쓰는 거 사는 거 추천
'''
1 단계 : 물리드라이버 세팅 
# C 드라이브 or D드라이브에 폴더 하나 만든다(ex: py1530) 그리고 거기에 
# 학습자료에 있는 chromedriver.exe를 넣어준다 (pdf파일에도 링크 있음)
# 파일 경로를 쓸 거기 때문에 경로는 알고 있어야됨 

2 단계 : 외부라이브러리 selenium, beautifulsoup 설치
# 윈도우키 + R키 -> cmd 창 띄우기
# pip install selenium --user  라고 입력
(외부라이브러리 설치 명령어 : pip install, --user은 윈도우 명령어. 관리자 권한으로 설치
pip install selenium 까지가 파이썬 명령어)

# 설치 다 됐으면 
# pip install beautifulsoup4 --user 입력

# 삭제는 pip uninstall ~~
'''

'''
from selenium import webdriver

1) webdriver.Chrome('경로')   와    .get("")
driver = webdriver.Chrome("chromedriver.exe 경로")
driver.get("이동하고 싶은 사이트")


2).find_element_by_xpath  와  .click()
login_btn = driver.find_element_by_xpath('웹정보의 xpath') 
login_btn.click() 


3) .send_keys('  ')
id_input = driver.find_element_by_xpath('웹정보의 xpath') 
id_input.send_keys('abc1234')
'''



# 셀레늄 모듈 임포트
from selenium import webdriver
import time



# 크롬 물리드라이버 가동 명령
driver = webdriver.Chrome("D:/py1530/chromedriver.exe") # webdriver 모듈에 있는 클래스 Chrome을 호출, Chrome의 객체를 생성.
# Chrome() 안에는 크롬 드라이버가 위치한 경로 써줌
# Chrome 클래스의 객체를 생성했으면 이 객체 정보를 어떤 변수에 담아줘야 사용가능
print("\n\n===== 드라이버의 타입은  : {}=====\n\n".format(type(driver))) # <class 'selenium.webdriver.chrome.webdriver.WebDriver'>
print("\n\n===== driver : {}=====\n\n".format(driver)) # <selenium.webdriver.chrome.webdriver.WebDriver (session="4c2ee6d2f054158ddd3542d6365898df")>

# 물리 드라이버로 사이트 이동명령
driver.get("https://www.naver.com") # 메서드 get 사용, 이동하고 싶은 사이트 적는다
# webdriver.Chrome("D:/py1530/chromedriver.exe").get("https://www.naver.com") 하면 오류뜨네... 

time.sleep(1)

# xpath를 이용하여 자동으로 클릭 제어하기
# xpath는 쉽게 말해서 웹에 있는 정보들의 주소, 경로라고 보면 된다
# xpath 값을 추출해야지만 자동으로 클릭을 제어하거나 자동으로 댓글을 달거나 할 수 있다

# 네이버의 로그인 버튼을 자동으로 누르게 하려면 로그인 버튼의 경로값을 알아야한다
# 네이버를 키고 f12를 누르면 뜨는 창의 왼쪽 상단에 사각형에 마우스 모양이 있는 아이콘이 있다
# (Select an element in the page to inspect it Ctrl+Shift+C)라고 뜨는 아이콘인데 그걸 누르고
# 네이버 로그인을 누르면 버튼에 위치한 소스코드가 잡힌다
# 그럼 그 부분을 우클릭 - Copy - Copy XPath 를 누르면 네이버 로그인 버튼에 대한 
# XPath 값을 추출할 수 있다
# 그럼 이제 파이썬으로 돌아와서 Ctrl+v 누른다

login_btn = driver.find_element_by_xpath('//*[@id="account"]/a') # find_element_by_xpath <- 메서드
# 안에 이미 "account" 쌍따옴표가 있으니까 ''로 문자열 형태로 넣어준다
# xpath 값을 문자열로 전달해주면 물리드라이버 웹브라우저에서 xpath값에 해당하는 element, data 요소를 찾아서 return해준다
# 그럼 우리는 그걸 변수에 저장

login_btn.click() # 클릭
# 위 두 줄을 한줄로 쓰려면 
# driver.find_element_by_xpath('').click()


# login_btn을 계속 재활용하고 쓸거면 저렇게 따로 변수로 저장해 놓고 
# 그게 아니라 한번만 쓰고 말거면 한줄에 한번에 쓰는게 편하다




# xpath를 이용하여 자동으로 텍스트 입력하기

time.sleep(2) # 페이지 로딩 시간을 고려하여 코드실행을 중단시킴
# 로딩이 안끝났는데 아래 코드를 작동시키면 제대로 작동 안 할수도 있다

id_input = driver.find_element_by_xpath('//*[@id="id"]') # 우리가 입력하고 싶은 창에 대한 XPath값 입력
# 네이버 아이디 입력창 XPath값 복붙
id_input.send_keys('abc1234')

time.sleep(2) # 페이지 로딩 시간을 고려하여 코드실행을 중단시킴
# 로딩이 안끝났는데 아래 코드를 작동시키면 제대로 작동 안 할수도 있다
pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
pw_input.send_keys('aaa1234')


# 이제 로그인 버튼 누르게 하면 자동 로그인 됨
# 프로듀스 48 투표도 time.sleep 24시간 돌려놓고 이렇게 자동으로 투표할 수 있다





'''
* 복습

s = "사과 바나나 복숭아"

print(s.split()) # 리스트
print(s.split()[1]) # 리스트니까 인덱싱 가능 -> 바나나
print(s.split()[1].find('바')) # '바나나' 문자열이니가 find 메서드 사용해서 0(정수)
print(s.split()[1].find('바') + 30) # 0 + 30 이나까 가능한 연산이다

type만 제대로 맞추면 .split.find .... 계속 할 수 있다
'''


