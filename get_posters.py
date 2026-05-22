import requests

api_key = '352ae29e'
movies = ['Demon Slayer: Kimetsu No Yaiba', 'Solo Leveling', "My Hero Academia: World Heroes' Mission", 'Attack on Titan']

for m in movies:
    res = requests.get(f'http://www.omdbapi.com/?t={m}&apikey={api_key}').json()
    print(f"{m}: {res.get('Poster')}")
