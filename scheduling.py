# pip install schedule

import schedule
import time
import crawl

# 10초에 한번씩 실행
schedule.every(10).second.do(crawl.testCrawl)
# 10분에 한번씩 실행
schedule.every(10).minutes.do(crawl.testCrawl)
# 매 시간 실행
schedule.every().hour.do(crawl.testCrawl)
# 매일 10:30 에 실행
schedule.every().day.at("10:30").do(crawl.testCrawl)
# 매주 월요일 실행
schedule.every().monday.do(crawl.testCrawl)
# 매주 수요일 13:15 에 실행
schedule.every().wednesday.at("13:15").do(crawl.testCrawl)

while True:
    schedule.run_pending()
    time.sleep(1)