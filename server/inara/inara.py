import requests
import json


def get_cmdr_info(apikey: str, cmdrname: str):
    # Define the API URL
    url = "https://inara.cz/inapi/v1/"  # Replace with the actual API endpoint

    # Prepare input JSON
    input_data = {
        "header": {
            "appName": "ArchitectsNotepad",
            "appVersion": "1.0",
            "APIkey": apikey,
        },
        "events": [
            {
                "eventName": "getCommanderProfile",
                "eventData": {
                    "searchName": "Niceygy"  # Replace with the desired commander name
                },
            }
        ],
    }
    # Send the POST request
    response = requests.post(url, json=input_data)

    # Check the response
    if response.status_code == 200:
        # Parse the JSON response

        data = response.text
        print(data)
        return json.decoder(data)    
    else:
        print(f"Error: {response.status_code}, {response.text}")
