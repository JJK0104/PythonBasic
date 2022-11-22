
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



# 셀레늄 모듈 임포트
from selenium import webdriver
import time



# 크롬 물리드라이버 가동 명령
driver = webdriver.Chrome("D:/py1530/chromedriver.exe") # webdriver 모듈에 있는 클래스 Chrome을 호출, Chrome의 객체를 생성.
# Chrome() 안에는 크롬 드라이버가 위치한 경로 써줌
# Chrome 클래스의 객체를 생성했으면 이 객체 정보를 어떤 변수에 담아줘야 사용가능
print("\n\n===== 드라이버의 타입은  : {}=====\n\n".format(type(driver))) # <class 'selenium.webdriver.chrome.webdriver.WebDriver'>
print("\n\n===== driver : {}=====\n\n".format(driver)) # <selenium.webdriver.chrome.webdriver.WebDriver (session="4c2ee6d2f054158ddd3542d6365898df")>


webdriver.Chrome("D:/py1530/chromedriver.exe").get("https://www.naver.com") 
# driver.get("https://www.naver.com") 
time.sleep(1)



login_btn = driver.find_element_by_xpath('//*[@id="account"]/a') 

login_btn.click()

time.sleep(2) 
id_input = driver.find_element_by_xpath('//*[@id="id"]') 
id_input.send_keys('abc1234')

time.sleep(2)
pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
pw_input.send_keys('aaa1234')


'''
* 복습

s = "사과 바나나 복숭아"

print(s.split()) # 리스트
print(s.split()[1]) # 리스트니까 인덱싱 가능 -> 바나나
print(s.split()[1].find('바')) # '바나나' 문자열이니가 find 메서드 사용해서 0(정수)
print(s.split()[1].find('바') + 30) # 0 + 30 이나까 가능한 연산이다

type만 제대로 맞추면 .split.find .... 계속 할 수 있다
'''


