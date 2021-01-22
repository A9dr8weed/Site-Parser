import requests
from bs4 import BeautifulSoup
from lxml import etree
import lxml.html

def get_html(url):
    r = requests.get(url)

    return r.text

def get_all_links(html):
    doc = lxml.html.document_fromstring(html)
    anchors = doc.xpath('//*[@id="content_grid-5"]/div//a')
    
    links = []
    for a in anchors:
        link = a.attrib.get('href')
        if link == "" or link is None or link == "#":
            continue
        links.append("https://www.marvel.com" + link + "/in-comics")

    return links

def get_h_content(html, urls):
    soup = BeautifulSoup(html, 'lxml')
    page_urls = soup.find_all("div", id = "__next")
    
    for url in page_urls:
        try:
            names = url.find_all("span", class_="masthead__headline")
            paragraphs = url.find_all("p", class_="railBioInfoItem__label")
            lis = url.find_all("ul", class_="railBioLinks")
            
            for name in names:
                nm = name.get_text()
                print("\n", nm)
                for paragraph in paragraphs:
                    p = paragraph.get_text()
                    print(p)
                for li in lis:
                    l = li.get_text()
                    print(l)
        except:
            nm = ""
            p = ""
            l = ""

def main():
    url = "https://www.marvel.com/characters"

    for url in get_all_links(get_html(url)):
        get_h_content(get_html(url), url)

if __name__ == '__main__':
    main()