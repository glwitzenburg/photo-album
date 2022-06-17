import json
import requests as requests
from nose.tools import assert_true


def request_response(album_id):
    response = requests.get('http://jsonplaceholder.typicode.com/photos?albumId=' + album_id)
    print_each_response(json.loads(response.text))
    assert_true(response.ok)


def print_each_response(response):
    for res in response:
        print(res["id"])
        print(res["title"])
        print("")
