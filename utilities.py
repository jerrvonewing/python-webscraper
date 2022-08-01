from bs4 import BeautifulSoup
import requests
import csv

#Go to given URL and extracy data
def scrapeData(url):
    try:
        source = requests.get(url)
        source.raise_for_status()

        #create soup 
        soup = BeautifulSoup(source.text,features='html.parser')

        #get contents from movies table
        movies = soup.find('tbody', class_='lister-list').find_all('tr')

        return movies
    except Exception as e:
        print(e)

#Take the etracted data and convert to CSV
def convertData(movies, header, filename):
    f = open(filename, "w")
    try:
        with open(filename,"a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for movie in movies:
                rank = movie.find('td', class_='titleColumn').get_text().strip().split('.')[0]
                name = movie.find('td', class_='titleColumn').a.text
                year = movie.find('td', class_='titleColumn').span.text.strip('()')
                rating = movie.find('td', class_='ratingColumn imdbRating').strong.text.strip()

                data = [rank, name, year, rating]
                writer.writerow(data)
        f.close()
    except Exception as e:
        print(e)