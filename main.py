from pprint import pprint

import requests

from yadisk import YaDisk
from reddit import Reddit


TEST_URL = 'https://www.cbr-xml-daily.ru/latest.js'


def test_request(url):
    response = requests.get(url)
    pprint(response.json())


YANDEX_TOKEN = ''

if __name__ == '__main__':
    # test_request(TEST_URL)
    # yadisk = YaDisk(YANDEX_TOKEN)
    # yadisk.get_files_list()
    # yadisk.upload_file('/new/test.txt', 'hello_world.txt')
    reddit = Reddit()
    reddit.get_latest_gifs()