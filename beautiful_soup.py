import requests
import lxml
import bs4
from page_url import PageUrl
from page_quote import PageQuote

class BeautifulSoup:
    url = ""
    url_list = []
    global pq

    def __init__(self, url):
        self.url = url
        if(url == PageUrl.QUOTES.value):
            self.pq = PageQuote()
        #if (url == PageUrl.BOOKS.value):
            #self.pq = BOOKS()
        pass

    def get_page_urls(self):
        i = 0
        while(True):
            i += 1
            new_url = self.url + self.pq.pagination_format.format(i)
            res = requests.get(new_url)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            if(len(soup.select(self.pq.quote_css)) != 0):
                self.url_list.append(new_url)
            else:
                break
        print('Number of page are: '+ str(len(self.url_list)))
    pass

    def get_data(self):
        data = []
        for page in self.url_list:
            res = requests.get(page)
            soup = bs4.BeautifulSoup(res.text, 'lxml')
            card_list = soup.select(self.pq.quote_css)

            for item in card_list:
                one_item = {}
                one_item.update({'quote': item.select(self.pq.text_css)[0].getText()})
                one_item.update({'author': item.select(self.pq.author_css)[0].getText()})
                #print(item.select(self.pq.text_css)[0].getText())
                #print(item.select(self.pq.author_css)[0].getText())
                list = []
                for i in item.select(self.pq.tag_css):
                    list.append(i.getText())
                    #print(i.getText())
                one_item.update({'tags': list})
                data.append(one_item)
        print(data)
        return data


