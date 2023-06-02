from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # this is the function that will be called when the user visits the index page
    # if the user submits the form on the index, page then the request method will be POST.
    if request.method == 'POST':
        # we can access the data the user submitted by using the request object
        artist_name = request.form['artist']
        # we can then pass this data to the search_albums function.
        albums = search_albums(artist_name)
        # we can then pass that on to results.html
        save_albums_to_db(artist_name, albums)
        return render_template('results.html', artist=artist_name, albums=albums)
    # if the user visit the index page without submitting the form,
    # then request method will be GET
    return render_template('index.html')
    order = False
    if "order" in request.form and request.form["order"] == "True":
        order = True
    if "order" in request.form and request.form["order"] == "False":
        order = False
    return render_template('results.html', artist=artist_name, albums=albums, sort=sort, order=order)
    return render_template('index.html')

def search_albums(artist_name):
    API_KEY = '523532'
    # URL = f'https://theaudiodb.com/api/v1.json/{API_KEY}/search.php?s={artist_name}'
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s={artist_name}'
    response = requests.get(URL)
    data = response.json()
    albums = data['album']
    return albums


def save_albums_to_db(artist_name, albums):
    conn = sqlite3.connect('albums.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS albums
                 (artist TEXT, album TEXT, year INTEGER)''')

    for album in albums:
        c.execute("INSERT INTO albums VALUES (?,?,?)", (artist_name, album['strAlbum'], album['intYearReleased']))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    app.run(debug=True)
