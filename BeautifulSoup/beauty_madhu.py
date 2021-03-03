##################################
    pip install beautifulsoup4
    
    Difference Between Parsers: https://goo.gl/zdy9br
    pip install lxml
    
    pip install html5lib
    
    pip install requests

#######################################



from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
  soup = BeautifulSoup(html_file, 'lxml')

print(soup)
print(soup.prettify())

match = soup.title
print(match)

match1 = soup.title.text
print(match1)

#finds the first div tag from the page

match2 = soup.div
print(match2)

match3 = soup.find(div, class_='footer')
print(match3)


article = soup.find(div, class_='article')
print(article)

headline = article.h2.a.text
summary = article.p.text

#####################

for article in soup.find_all(div, class_='article')
  headline = article.h2.a.text
  print(headline)
  summary = article.p.text
  print(summary)
  
  



