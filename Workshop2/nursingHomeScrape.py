import requests
from bs4 import BeautifulSoup

page = requests.get('https://projects.propublica.org/nursing-homes/')
soup = BeautifulSoup(page.content, 'html.parser')
tables = soup.find_all(class_="fines-summary")
nursingHomesFines = tables[0].find_all("a")
nursingHomesDeficiencies = tables[1].find_all("a")
stories = soup.find_all(id="nh_local_stories")[0].find_all("a")

print("Nursing homes with the most fines:")
for i in range(len(nursingHomesFines)):
    print(f"{i + 1}. {nursingHomesFines[i].get_text()}")

print()

print("Nursing homes with the most serious deficiencies:")
for i in range(len(nursingHomesDeficiencies)):
    print(f"{i + 1}. {nursingHomesDeficiencies[i].get_text()}")

print()

print("Top 5 news stories on nursing homes with the most fines and/or serious deficiencies:")
for i in range(5):
    print(f"{i + 1}. {stories[i].get_text()}: {stories[i]['href']}")