import requests
import pprint

# Replace with your info
SHEET_ID = "13h0byn3IyOk-rN2fNrHS5zNUVJD_gnWqYDXLMEeyNmA"
API_KEY = "AIzaSyB2EaB-g06MebzkcyNeY0ibxBF3QVnSOqs"
RANGE = "form2"  # adjust range & sheet name as needed

# Build the URL
url = f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{RANGE}?key={API_KEY}"

# Send GET request
response = requests.get(url)

# Parse and print
if response.status_code == 200:
    data = response.json()
    values = data.get("values", [])
    print(values[0][0])
    if values[2][2] == "AAA":
        print("a")
    else:
        print("b")
    if values[3][2] == "BBB":
        print("c")
    if values[6][2] == "BBB":
        print("d")

