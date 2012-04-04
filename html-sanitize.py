import sys
from BeautifulSoup import BeautifulSoup

def keep_only_bold_italic(style):
    res = ''

    if style.find('font-weight:bold') >= 0:
        res += 'font-weight:bold;'
 
    if style.find('font-style:italic') >= 0:
        res += 'font-style:italic;'

    return res

def sanitize_style(tag):
    if tag.has_key('style'):
        style = keep_only_bold_italic(tag['style'])
        if len(style) > 0:
            tag['style'] = style
        else:
            del tag['style']

def sanitize_html(value):
    soup = BeautifulSoup(value)

    for tag in soup.findAll(True):
        sanitize_style(tag)
        del tag['class']
        del tag['id']
        del tag['dir']

    return soup.renderContents()

if __name__ == "__main__":
    data = sys.stdin.readlines()
    html = '\n'.join(data)
    print sanitize_html(html)
