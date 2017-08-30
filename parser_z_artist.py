"""
Notes

Tutorial Link: https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3

"""
import requests
from bs4 import BeautifulSoup

# collect first page of artists' list
page = requests.get('https://www.nga.gov/collection/anZ1.htm')

# Create a beautiful soup object
soup = BeautifulSoup(page.text, 'html.parser')

# We need to remove the Navigation links at the bottom of the page to only get just the artist names.
navigation_links = soup.find(class_='AlphaNav')
# decompose removes a tag from the parse tree and then destroys it along with its contents
navigation_links.decompose()

artist_name_list = soup.find(class_='BodyText')

artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    # print(artist_name.prettify())
    print(artist_name.text)





