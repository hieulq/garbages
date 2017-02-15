import newspaper
from newspaper import Article

import requests
from dragnet import content_extractor, content_comments_extractor

from eatiht import etv2
from eatiht import v2
import eatiht

from readability.readability import Document
import urllib
from bs4 import BeautifulSoup

TARGET = 'http://giaitri.vnexpress.net'
# ARTICLE = 'http://suckhoe.vnexpress.net/tin-tuc/dinh-duong/uong-nuoc-lanh' \
#          '-giup-giam-can-3536234.html'
ARTICLE = 'http://www.baomoi.com/ios-cach-khac-phuc-van-de-dinh-ma-doc-tu' \
          '-redirect-quang-cao-khi-vao-bat-ki-website-nao/c/19620631.epi'
# ARTICLE = 'https://vnhacker.blogspot.com/2017/01/nuoc-my-va-nguoi-nhap-cu' \
#           '.html'


# Dragnet only works with py27
def try_dragnet():
    # fetch HTML
    r = requests.get(ARTICLE)
    # get main article without comments
    content = content_extractor.analyze(r.content)
    print("======")
    print(content)
    # get article and comments
    content_comments = content_comments_extractor.analyze(r.content)
    print("======")
    print(content_comments)


def try_newspaper():
    vne = newspaper.build(TARGET)
    a = Article(ARTICLE, language='vi')
    for article in vne.articles:
        print(article.url)

    a.download()
    a.parse()
    print("FIN")


def try_readability():
    html = urllib.request.urlopen(ARTICLE).read()

    doc = Document(html)
    con = BeautifulSoup(doc.summary()).get_text()
    tit = doc.short_title()
    print("===READABILITY===")
    print("=CONTENT=")
    print(con)
    print("=TITLE=")
    print(tit)


def try_eatiht():
    print("===EATIHT V2===")
    tree = etv2.extract(ARTICLE)
    tree.bootstrapify()
    print(tree.get_html_string())

    print("===V2===")
    print(v2.extract(ARTICLE))

    print("===V1===")
    print(eatiht.extract(ARTICLE))


def main():
    try_newspaper()


if __name__ == '__main__':
    if __name__ == '__main__':
        main()

# newspaper load target --> detect categories --> cached --> filter by domain
# --> detect article list --> filter for remove temp URL (#, ?..) --> pick
# random articles and detect format --> validate format --> send to worker
# --> worker start crawling --> if error happen, notify back to master
