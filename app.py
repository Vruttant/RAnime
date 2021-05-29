import random
from flask import Flask, render_template
from jikanpy import Jikan
from datetime import date
app = Flask(__name__)
jikan = Jikan()



def getRandomYear(years_old=5):
    current_year = date.today().year
    random_year = random.randint(current_year - years_old, current_year)
    return random_year

def getRandomSeason():
    list_of_seasons = ["summer", "spring", "fall", "winter"]
    random_season = random.choice(list_of_seasons)
    return random_season

def getRandomAnimeList():
    global filter_year
    global filter_season
    filter_year = getRandomYear(random.randint(5,10))
    filter_season = getRandomSeason()
    random_animes = jikan.season(year=filter_year, season=filter_season)
    return random_animes

@app.route('/')
def home():
    return render_template('home.html', title="Home", anime_list=getRandomAnimeList(), season=filter_season, year=filter_year)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run()
