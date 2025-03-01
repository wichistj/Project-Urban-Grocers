
import configuration
import requests

def get_new_user_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH)
    return response.json().get("authToken")

def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=kit_body, headers=headers)
    return response
