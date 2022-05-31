# Third-party imports...
import json

import requests as requests
from nose.tools import assert_true


def test_request_response(id):
    # Send a request to the API server and store the response.
    response = requests.get('http://jsonplaceholder.typicode.com/photos?albumId=' + id)
    y = json.loads(response.text)
    # print(y['id'])

    # Confirm that the request-response cycle completed successfully.
    print_each_response(json.loads(response.text))
    assert_true(response.ok)

def print_each_response(response):
    for res in response:
        print(res["id"])
        print(res["title"])
        print("")
