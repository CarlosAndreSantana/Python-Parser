# Sona Eveningstar Jorge Candeu, 769802
# Carlos Andre Costa Santana, 773370
# Lucas Mathaeus Pereira, 726561

from bs4 import BeautifulSoup
import urllib.request
import csv
from datetime import datetime

class Open:
    def fun_soup(self, site):
        fp = urllib.request.urlopen(site)
        html_doc = fp.read().decode("utf8")
        fp.close()
        return BeautifulSoup(html_doc, 'html.parser')

class Writer:
    def __init__(self, Open):
        self.Open = Open

    def write(self, site, parser = "soup"):
        with open(f"dump-{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.csv", mode='w') as csv_file:
            if site == "https://www.bol.uol.com.br/" and parser == "soup":
                csv_writer = csv.writer(csv_file, delimiter=';')
                csv_writer.writerow(['category', 'title', 'link'])
                soup = self.Open.fun_soup(site)
                for title in soup.select(".thumb-title"):
                    parent = title.parent
                    while True:
                        if parent.has_attr('class'):
                            if "highlights-headline" != parent['class'][0]:
                                parent = parent.parent
                            else:
                                break
                        else:
                            parent = parent.parent
                    if(parent.div.next_sibling != None):
                        category = parent.div.div.div.div.div.h3.find_all('a')[0].span.get_text()
                    else:
                        category = "Principal"   
                    csv_writer.writerow([category, title.get_text(), title.parent.parent.get('href')])
            #elif site == "link.com" and parser == "parser":

Open = Open()
Writer = Writer(Open)

Writer.write("https://www.bol.uol.com.br/")