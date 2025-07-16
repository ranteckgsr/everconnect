import requests
from requests.auth import HTTPBasicAuth

site_url = "https://everconnect.ca"
form_id   = 23031
status    = "publish"

url = f"{site_url}/wp-json/custom-evf/v1/entries?form_id={form_id}&status={status}"

username = "German"               
app_password = "cTp1 3AMd qnAA YYtw uHOb wshz" 

response = requests.get(url, auth=HTTPBasicAuth(username, app_password))

import json

if response.ok:
    entries = response.json()
    print(f"Total entries found: {len(entries)}")
    if entries:
        print("\nAll entries:")
        for i, entry in enumerate(entries, 1):
            print(f"\nEntry {i}:")
            try:
                fields = json.loads(entry.get('fields', '{}'))
                first_name = next((v for k, v in fields.items() if v.get('type') == 'first-name'), None)
                phone_number = next((v for k, v in fields.items() if v.get('type') == 'number'), None)
                file_upload = next((v for k, v in fields.items() if v.get('type') == 'file-upload'), None)

                print("  First Name :", first_name['value'] if first_name else 'N/A')
                print("  Phone Number:", phone_number['value'] if phone_number else 'N/A')
                if file_upload:
                    print("  File Upload :", file_upload.get('value'))
                else:
                    print("  File Upload : N/A")
            except Exception as e:
                print(f"Error parsing fields for entry {i}: {e}")
    else:
        print("No entries found.")
else:
    print("Error:", response.status_code, response.text)
