from bs4 import BeautifulSoup
import requests

#Section 1: Make an HTTP request to get the content of the Federal Register's contents page
url = "http://[URL for the federal register]"
r  = requests.get(url)

#Section 2: Turn the content into text, and then cook it down to a soup we can work with
data = r.text
soup = BeautifulSoup(data)

#Section 3: Stir up the soup and grab titles/headlines, org names, summary text, and/or the links to the pdfs
all_links = soup.find_all('a')

#Section 4: Parse simple HTML


#Section 5: Open pdfs and parse that data


#Section 6: Do something else with the data (i.e. move to database)
print all_links
