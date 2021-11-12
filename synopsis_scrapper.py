# This code allows us to search films by their title 
# and access their written scripts as a text file
# By Saimat Balabekova

from bs4 import BeautifulSoup
import requests

# Asks user for the film
search_film = input("Film Title: ")

# Make request to the search url with the film title
search_url = "https://subslikescript.com/search?q=" + search_film.replace(" ","+")
search_result = requests.get(search_url)
search_result = search_result.text

# Parse through the search result and get the link for the film
search_soup = BeautifulSoup(search_result, "html.parser")
film_list = search_soup.find("ul", class_= "scripts-list")
film = film_list.find_all("a")[0]
film_id = film["href"]

# Gets the script website of desired content
website = "https://subslikescript.com/" + film_id
result = requests.get(website)
content = result.text   #content of the website

# make a soup object for script website
soup = BeautifulSoup(content, 'html.parser')

# Find the script location
main_article = soup.find("article", class_="main-article")

# Extract the title and script
title = main_article.find('h1').get_text().lower().replace(" ","_")
script = main_article.find('div', class_="full-script").get_text("\n")

# Save to file with the name of the film
with open(f'{title}.txt', 'w', encoding="utf-8") as f:
    f.write(script)