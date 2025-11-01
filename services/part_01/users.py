import requests

API_KEY = "reqres-free-v1"
HEADERS = {"x-api-key": API_KEY}

def get_user(id):
    url = f"https://reqres.in/api/users/{id}"
    session = requests.session()
    response = session.get(url, headers=HEADERS)
    return response

def get_users_list(page_id):
    url = "https://reqres.in/api/users"
    session = requests.session()
    response = session.get(url, headers=HEADERS, params={'page': page_id})
    return response
