from bs4 import BeautifulSoup

with open('outputDiv.html', 'r', encoding="utf8") as f:
	contents = f.read()
	soup = BeautifulSoup(contents, features="html5lib")

def check_class(soup):
	
	class_Soup = set()

	tags = {tag.name for tag in soup.find_all()}

	for tag in tags:
		for i in soup.find_all( tag ):
			if i.has_attr( "class" ):
				if len( i['class'] ) != 0:
					class_Soup.add(" ".join( i['class']))
	return class_Soup

def In_File_Div(class_Soup):
	with open("outputDiv.txt", "w", encoding='utf-8') as file:
		return (file.write(str(class_Soup)))

def main():
	class_Soup = check_class(soup)
	In_File_Div(class_Soup)

if __name__ == '__main__':
	main()