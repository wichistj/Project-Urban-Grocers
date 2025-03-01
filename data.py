headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {authToken}"
}

kit_model = {
    "name"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

valid_kit_name_1 = {"name": "a"}
valid_kit_name_511 = {
    "name": "Abcd" * 127 + "abc"
}
invalid_kit_name_0 = {"name": ""}
invalid_kit_name_512 = {
    "name": "Abcd" * 128
}
valid_kit_name_special_chars = {"name": "№%@,"}
valid_kit_name_spaces = {"name": " A Aaa "}
valid_kit_name_numbers = {"name": "123"}
invalid_kit_missing_name = {}
invalid_kit_wrong_type = {"name": 123}