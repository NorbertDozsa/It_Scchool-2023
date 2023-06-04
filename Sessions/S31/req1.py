import requests
import time

URL = "https://jsonplaceholder.typicode.com/"
POST_URL = "https://jsonplaceholder.typicode.com/posts"
COMMENT_URL = "https://jsonplaceholder.typicode.com/comments"

def get_with_retry(url):

    try:    
        resp = requests.get(url, timeout=(3.5, 30))
    except requests.ConnectTimeout:
        print("Connection timed out. Retrying after 3 sec.")
        time.sleep(3)
        get_with_retry(url)
    else:
        resp.raise_for_status()
        return resp.json()
    
def get(url):
    resp = requests.get(url, timeout=(3.5, 30))
    resp.raise_for_status()
    return resp.json()

try:
    get_with_retry(COMMENT_URL)
except requests.exceptions as err:
    print(err)