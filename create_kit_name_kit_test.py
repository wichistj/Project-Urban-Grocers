import sender_stand_request
import data

def auth_token():
    return sender_stand_request.get_new_user_token()

def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_kit_name_1_char():
    positive_assert(data.valid_kit_name_1, auth_token())

def test_kit_name_511_chars():
    positive_assert(data.valid_kit_name_511, auth_token())

def test_kit_name_special_chars():
    positive_assert(data.valid_kit_name_special_chars, auth_token())

def test_kit_name_spaces():
    positive_assert(data.valid_kit_name_spaces, auth_token())

def test_kit_name_numbers():
    positive_assert(data.valid_kit_name_numbers, auth_token())

# Pruebas negativas
def test_kit_name_0_chars():
    negative_assert_code_400(data.invalid_kit_name_0, auth_token())

def test_kit_name_512_chars():
    negative_assert_code_400(data.invalid_kit_name_512, auth_token())

def test_kit_missing_name():
    negative_assert_code_400(data.invalid_kit_missing_name, auth_token())

def test_kit_wrong_type():
    negative_assert_code_400(data.invalid_kit_wrong_type, auth_token())