


from selenium import webdriver
import time

driver = webdriver.Chrome('D:/py1530/chromedriver.exe')
driver.get('https://www.naver.com')

driver.find_element_by_xpath('//*[@id="news_cast"]/div[1]/ul/li[1]/a').click()

time.sleep(1)


for x in range(6):
    news_tab = '//*[@id="right.ranking_tab_10%d"]' % x
    
    for n in range(1, 6):
        news_rank = '//*[@id="right.ranking_contents"]/ul/li[%d]/a' % n
        driver.find_element_by_xpath(news_tab).click()
        driver.find_element_by_xpath(news_rank).click()
        time.sleep(1)








