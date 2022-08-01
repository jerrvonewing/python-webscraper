import datetime
import utilities as util

url = 'https://www.imdb.com/chart/top/'
today = datetime.date.today()
filename = './IMDb Top 250 Movies ' + str(today) + '.csv'
header = ['Rank','Name', 'Year', 'Rating']
movies = util.scrapeData(url)
util.convertData(movies,header, filename)
