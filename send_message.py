import requests
import json
from config import PRODUCT_ID, PHONE_ID, API_KEY

def send_whatsapp_message(to_number, message):
    url = f"https://api.maytapi.com/api/{PRODUCT_ID}/{PHONE_ID}/sendMessage"
    
    payload = json.dumps({
        "to_number": to_number,
        "type": "text",
        "message": message
    })
    
    headers = {
        'Content-Type': "application/json",
        'x-maytapi-key': API_KEY
    }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    return response.json()

# Example usage
if __name__ == "__main__":
    result = send_whatsapp_message("905301234567", "Hello World from Python!")
    print(json.dumps(result, indent=2))