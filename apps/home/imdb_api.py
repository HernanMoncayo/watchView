import requests

def get_movie_data(movie_name):
    url = "https://imdb8.p.rapidapi.com/auto-complete"
    querystring = {"q": movie_name}
    headers = {
        "X-RapidAPI-Key": "552f27f1aamshf37f9a209d853fap128fd0jsnb077d1a4b9cd",
        "X-RapidAPI-Host": "imdb8.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()
