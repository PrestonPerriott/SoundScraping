import requests
from bs4 import BeautifulSoup
base_url = 'https://soundcloud.com{}' #{} is a place holder fofr when we decide to use base_url.format to concate the link
url = 'https://soundcloud.com/preston-perr/likes'
response = requests.get(url)  #queries url
html = response.content   #saves url html code in variable html
soup = BeautifulSoup(html) #parses the html code for Beautiful soup use

print (soup.prettify())  #print the html code in a nice neat beautiful soup format
table = soup.findAll('a')  #saves all <a> of html file in variable table
#print (table.prettify())
print(soup.title)      #prints the title of html doc
print(soup.a)         #prints the <a> attributed items of html code
print(table)
##


for link in soup.find_all("a"):   #for statement that finds and prints the links in html code
    print(link.text)
    print(base_url.format(link.get('href')))
 #stuff = link.get('href')  #stores the found links in stuff
   #print(stuff)     #prints the links we found "stuff"
# print(link.get('href'))

stuff = []
stuff = (link.get('href'))
 #print(stuff)






#print(stuff[0:6])    #attempting to print a specific item in stuff
#print(len(stuff))