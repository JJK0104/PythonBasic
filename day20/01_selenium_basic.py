


# 셀레늄 모듈 임포트
from selenium import webdriver
import time

# 크롬 물리드라이버 가동 명령
driver = webdriver.Chrome("D:/py1530/chromedriver.exe")

# 물리 드라이버로 사이트 이동명령
driver.get("https://www.naver.com")

time.sleep(1)
# xpath를 이용하여 자동으로 클릭 제어하기
login_btn = driver.find_element_by_xpath('//*[@id="account"]/div/a/i')
login_btn.click()

# driver.find_element_by_xpath('').click()

# xpath를 이용하여 자동으로 텍스트 입력하기
time.sleep(2)
id_input = driver.find_element_by_xpath('//*[@id="id"]')
id_input.send_keys('abc1234')

time.sleep(2)
pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
pw_input.send_keys('aaa1234')









