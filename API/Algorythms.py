

@app.route ('/', methods=['GET', 'POST'])
def search():
    # BEGIN Search
    # INPUT Artist as artist_name OR artist_name = Input Artist
    artist_name = request.form['artist']
    # VAR url = https://theaudiodb.com/api/v1/json/{523532}/searchalbum.php?s={artist_name}
    URL = f'https://theaudiodb.com/api/v1/json/{API_KEY}/searchalbum.php?s={artist_name}'
    # VAR response = GET artist_data from url
    response = requests.get(url)
    # print(type(response))
    # print(response)
    # VAR data = format response
    data = response.json()
    # print(type(data))
    # print(data
    # Display data AS results.html
    return render_template('results.html', artist=artist_name, albums=albums)



