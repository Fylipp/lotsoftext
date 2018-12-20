import lxml.etree
import requests

from lotsoftext.article import Article


def get_random():
    r = requests.get('https://en.wikipedia.org/wiki/Special:Random')

    if r.status_code != 200:
        raise Exception(f'Non-OK status code: {r.status_code}')

    tree = lxml.etree.fromstring(r.text)

    url = text_format(r.url)

    title = tree.xpath("//h1[@id='firstHeading']/text()")
    if len(title) < 1:
        raise Exception('Article page is missing its title')
    title = text_format(title[0])

    text_elements = tree.xpath("//div[@id='mw-content-text']/div[@class='mw-parser-output']/*")
    if len(text_elements) < 1:
        raise Exception('Article page is missing its text')
    content = ''
    for text_element in text_elements:
        if text_element.tag in ['p', 'a']:
            content += ''.join(text_element.itertext())
    content = text_format(content)

    return Article(url, title, content)


def text_format(text):
    return ' '.join(text.strip().split())
