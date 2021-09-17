import requests


def crawl(target_url, filename):
    response = requests.get(target_url)
    html = response.content.decode('utf-8').strip()
    f = open(filename, 'w')
    f.write(html)
    f.close()


crawl("https://github.com/", "crawler.html")
