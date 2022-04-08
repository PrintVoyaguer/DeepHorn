import requests
from bs4 import BeautifulSoup

#Permet d'éviter trop de scraping donc de faire des loops permetant de programmer des horaires de scraping pour IA

url = 'https://store.steampowered.com'

	#Check Data import data from url to soup
def Check_Data(url):
	http_page = requests.get(url)
	soup = BeautifulSoup(http_page.text, 'lxml')
	return (soup)

	#Use htmlPage to html file
def In_File_Data(soup):
	with open("outputData.html", "w", encoding='utf-8') as file:
		return (file.write(str(soup)))

def check_Div(soup):
	div = soup.find_all("div")
	return (div)

def In_File_Div(div):
	with open("outputDiv.html", "w", encoding='utf-8') as file:
		return (file.write(str(div)))

	#Main fonction for use my def
def main():
	#Use variable for def
	soup = Check_Data(url)
	div = check_Div(soup)
	#Print in to doc
	fileData = In_File_Data(soup)
	fileDiv = In_File_Div(div)

if __name__ == '__main__':
	main()