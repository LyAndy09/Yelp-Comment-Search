import requests
from bs4 import BeautifulSoup
import GetURL
import lxml
import cchardet
import time

g = GetURL

urls = g.filtered_urls

results = []
records = []
for i in range(len(urls)):
    r = requests.get(urls[i])
    soup = BeautifulSoup(r.text, 'lxml')
    text = soup.find_all('span', attrs={'class':'raw__09f24__T4Ezm'})
    records.append(text)


print(records[4])
print(results[4])


# results = []
# for link in range(len(url_list)):
#     temp = []
#     r = requests.get(url_list[link])
#     soup = BeautifulSoup(r.text, 'xml')
#     text = soup.find_all("p", class_="comment__09f24__gu0rG css-qgunke")
#     temp.append(text)
#     results.append(temp)
#
# print(*results, sep = '\n')
#print(*filtered_urls, sep = '\n')

# for link in range(len(url_list)):
#      temp = []
#      r = requests.get(url_list[link])
#      r.text
#      soup = BeautifulSoup(r.text, 'html.parser')
#      text = soup.get_text()



#print(text)

#print(divs)
# r = requests.get('https://www.yelp.com/biz/nothing-but-coffee-los-angeles?osq=Coffee+%26+Tea')

#print(r.status_code)

#r.text
#print(r.text)
#soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
#divs = soup.findAll(class_='raw__09f24__T4Ezm')

# review = []
# for div in divs:
#    review.append(div.text)

#print(review)

