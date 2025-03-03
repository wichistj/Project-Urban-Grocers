import data
import configuration
import requests

def get_new_user_token():
    headers =  data.headers.copy()
    user_body = data.user_body.copy()
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, headers=headers, json=user_body)
    return response.json().get("authToken")

def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=kit_body, headers=headers)
    return response
