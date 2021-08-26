# pip install requests beautifulsoup4

import urllib.request
from bs4 import BeautifulSoup
import ssl # https 에서 받아오는 경우

# html 내용 받아오는 함수
def testCrawl():
    # https 에서 받아오는데 에러가 발생할 경우
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
    # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

    url = 'html 필요한 url 주소'
    html = urllib.request.urlopen(url).read()
    global soup
    soup = BeautifulSoup(html, 'html.parser')

    # soup 에 html 내용 저장
    print(soup)

# 받아온 html에서 필요한 부분 가져와서 text에 저장하는 함수
def getFromTag():

    print(soup.p) # 첫번째 p 태그 출력
    print(soup.p.string) # 첫번째 p 태그의 내용만 출력
    
    for child in soup.ul.children: # ul 태그의 하위 항목 모두 출력
        print(child)

    for parent in soup.ul.parents: # ul 태그의 상위 항목 모두 출력
        print(parent)

    print(soup.find_all('h2')) # h2 태그 모두 출력

    print(soup.find_all(attrs = {'class' : 'form'})) # form 이라는 이름의 class인 태그만 모두 출력


testCrawl()
getFromTag()
