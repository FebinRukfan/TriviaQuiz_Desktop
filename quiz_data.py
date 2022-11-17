import requests

parameters = {
    "amount": 30,
    "category": 28,
    "difficult": "medium",
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]