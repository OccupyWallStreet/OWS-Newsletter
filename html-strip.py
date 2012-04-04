import sys
from BeautifulSoup import BeautifulSoup

def strip_html(value):
    soup = BeautifulSoup(value, convertEntities=BeautifulSoup.HTML_ENTITIES)

    res = ''
    links_to_insert = []

    for tag in soup.findAll(True):
        if tag.name == 'a' and tag.has_key('href'):
            href = tag['href']
            if len(href) > 4 and href[:4] == 'http':
                links_to_insert.append(href)

        if tag.string:        
            res += tag.string

        if tag.name in ('p', 'br'):
            # we take URLs from <a> tags and insert them, each on their own line, after the next paragraph end
            if len(res) > 0 and res[-1] == '\n':
                for link in links_to_insert:
                    res += (link + '\n')
                links_to_insert = []                

            res += '\n'

    return res.encode("utf-8")

if __name__ == "__main__":
    data = sys.stdin.readlines()
    html = '\n'.join(data)
    print strip_html(html)
