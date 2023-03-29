from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import datetime, time

def kyochon_store(result):
    for sido in range(1,18):
      for gu in range(1,46):
        try:
          kyochon_url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (sido, gu)
          html = urllib.request.urlopen(kyochon_url)
          soupKyochon = bs(html, 'html.parser')
          ul_tag = soupKyochon.find("div", {"class": "shopSchList"})

          for store_data in ul_tag.findAll('a'):
            store_name = store_data.find('strong').get_text()
            store_address = store_data.find('em').get_text().strip().split('\r')[0]
            store_sido, store_gu = store_address.split()[0], store_address.split()[1]
            result.append([store_name] + [store_sido] + [store_gu] + [store_address])
        except:
          pass


def main():
  result = []
  kyochon_store(result)
  kyochon_tbl = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
  kyochon_tbl.to_csv('C:\\Users\\LimJiSeon\\OneDrive\\바탕 화면\\test\\test.csv', encoding='cp949', mode='w', index=True)
  del result[:]


if __name__ == '__main__':
  main()
