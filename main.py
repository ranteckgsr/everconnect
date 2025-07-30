from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import RedirectResponse
from requests.auth import HTTPBasicAuth
import requests
import json

app = FastAPI(
    title="Everest Forms API",
    description="API to fetch Everest Forms entries",
    version="1.0.0"
)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

@app.get("/entries")
def get_entries(form_id: int = Query(...), status: str = "publish"):
    site_url = "https://everconnect.ca"
    url = f"{site_url}/wp-json/custom-evf/v1/entries?form_id={form_id}&status={status}"

    username = "German"
    app_password = "cTp1 3AMd qnAA YYtw uHOb wshz"

    response = requests.get(url, auth=HTTPBasicAuth(username, app_password))
    if not response.ok:
        return {"error": response.text}

    entries = response.json()
    results = []
    for entry in entries:
        fields = json.loads(entry.get('fields', '{}'))
        first_name = next((v for k, v in fields.items() if v.get('type') == 'first-name'), None)
        phone_number = next((v for k, v in fields.items() if v.get('type') == 'number'), None)
        file_upload = next((v for k, v in fields.items() if v.get('type') == 'file-upload'), None)
        results.append({
            "First Name": first_name['value'] if first_name else None,
            "Phone Number": phone_number['value'] if phone_number else None,
            "File Upload": file_upload.get('value') if file_upload else None
        })
    return {"entries": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)