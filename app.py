from flask import Flask, render_template
import json
import datetime
import utilities as util

app = Flask(__name__)
@app.route('/')
def main():
    url = 'https://www.imdb.com/chart/top/'
    today = datetime.date.today()
    filename = './IMDb Top 250 Movies ' + str(today) + '.csv'
    header = ['Rank','Name', 'Year', 'Rating']
    movies = util.scrapeData(url)
    util.convertData(movies,header, filename)
    filePath = '/../' + filename
    print(filePath)

    return render_template('index.html', filePath=filePath)
