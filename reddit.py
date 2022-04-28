import requests


class Reddit:
    def get_latest_gifs(self):
        url = 'https://www.reddit.com/r/gifs/top.json?t=day'
        headers = {'User-Agent': 'netology'}
        response = requests.get(url, headers=headers)
        print(response.json())