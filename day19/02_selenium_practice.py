# 이거 할 때마다 사이트가 업데이트 되고 변하기 때문에 직접 찾아가면서 하는 거 추천


from selenium import webdriver
import time

driver = webdriver.Chrome('D:/py1530/chromedriver.exe')
driver.get('https://www.naver.com')
time.sleep(2)

# 네이버 스포츠 클릭
driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[3]').click()
time.sleep(2)
# 네이버 해외축구 클릭
driver.find_element_by_xpath('//*[@id="_sports_lnb_menu"]/div/ul[1]/li[5]/a').click()


time.sleep(3) # 페이지 로딩 시간을 고려하여 코드실행을 중단시킴
# 로딩이 안끝났는데 아래 코드를 작동시키면 제대로 작동 안 할수도 있다

# 들어왔으면 이제 이시각 많이 본 뉴스를 1위~ 10위 자동으로 누르게 하기 
'''
1위 XPath 
//*[@id="content"]/div/div[1]/div[2]/div/ol/li[1]/a
2위 XPath
//*[@id="content"]/div/div[1]/div[2]/div/ol/li[2]/a
5위 XPath
//*[@id="content"]/div/div[1]/div[2]/div/ol/li[5]/a
10위 XPath
//*[@id="content"]/div/div[1]/div[2]/div/ol/li[10]/a

보니까 일종의 패턴이 보인다. 보통 이런 것들은 다 패턴이 있다
'''


for n in range(1, 11):

    '''
    아래코드를 실행하면 1번기사만 클릭되고 나머지는 작동 안함.
    이유는 1번기사로 들어가봐라
    근데 1번기사에서는 2번기사 주소로 한번에 못감... 가려면 다시 <해외축구>란으로 갔다가 2번으로 가거나 
    옆에 작은 란에 있는 2번째 기사로 가야되는 여기서의 2번 기사가 <해외축구>란에서 보는 2번기사 xpath값이 다름
    
    '''
    
    news_rank = '//*[@id="content"]/div/div[1]/div[2]/div/ol/li[%d]/a' %n
    rank_path = driver.find_element_by_xpath(news_rank)
    rank_path.click()
    time.sleep(1) # 페이지 로딩 시간을 고려하여 코드실행을 중단시킴
    # 로딩이 안끝났는데 아래 코드를 작동시키면 제대로 작동 안 할수도 있다
    print("%d번 기사를 클릭완료했습니다."%n)
    

'''
rank = []
for n in range(1,11):
    news_rank = '//*[@id="content"]/div/div[1]/div[2]/div/ol/li[%d]/a' %n
    rank.append(news_rank)
'''
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/div/ol/li[1]/a').click()
time.sleep(1.5)
print("\n\n\n1번 기사 클릭 완료\n\n\n")
driver.find_element_by_xpath('//*[@id="_ranking_news_list_0"]/li[2]/a/span').click()
time.sleep(1.5)
print("\n\n\n2번 기사 클릭 완료\n\n\n")

'''

# 그럼 이제 야구, 해외야구, 해외축구, 축구의 각 1~10위 기사를 눌러보자
# 네이버는 해외축구 2위 누르면 자동으로 야구란으로 옮겨져서 
# 해외축구 누르고 1위 누르고/ 다시 해외축구 누르고 2위 누르고/ 해외축구 누르고 3위 누르고 ~~
# 이런식으로 만들어보자 

# 야구, 해외야구, 해외축구 등에서도 유사성이 발견된다
for x in range(6):
    news_tab = '//*[@id="right.ranking_tab_10%d"]' % x
    
    for n in range(1, 6):
        news_rank = '//*[@id="right.ranking_contents"]/ul/li[%d]/a' % n
        driver.find_element_by_xpath(news_tab).click() # 탭 누르고
        driver.find_element_by_xpath(news_rank).click() # 기사 누르고
        time.sleep(1)


'''





