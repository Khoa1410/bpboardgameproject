import requests
import pprint
import pandas as pd 
import numpy as np
# Replace with your info
SHEET_ID = "13h0byn3IyOk-rN2fNrHS5zNUVJD_gnWqYDXLMEeyNmA"
API_KEY = "AIzaSyB2EaB-g06MebzkcyNeY0ibxBF3QVnSOqs"
RANGE = "form3"  # adjust range & sheet name as needed

# Build the URL
url = f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{RANGE}?key={API_KEY}"
# url = "https://docs.google.com/spreadsheets/d/13h0byn3IyOk-rN2fNrHS5zNUVJD_gnWqYDXLMEeyNmA/edit?resourcekey=&gid=1557762788#gid=1557762788"
response = requests.get(url)

# Parse and print
if response.status_code == 200:
    data = response.json()
    values = data.get("values", [])
    # print(values[0][0])
    # if values[2][2] == "AAA":
    #     print("a")
    # else:
    #     print("b")
    # if values[3][2] == "BBB":
    #     print("c")
    # if values[6][2] == "BBB":
    #     print("d")

special_voter = {
    "name": "Chinh",
    "vote": [5,3,9,5,6,7,1,3,4,6]
}
def process_data(special_voter: dict, data, n = 3):
    if len(data["values"]) <=1:
        return []
    df = pd.DataFrame(data["values"][1:],columns=data["values"][0])
    special_voter_vote = special_voter.get("vote", [])
    if len(special_voter_vote) == 0:
        df["point"] = 0
       
        return [df[["name","point"]].to_dict("records")]
    list_of_players_data = df.iloc[:, 1:12].values.tolist()
    output_data = []
    try:
        for player_datum in list_of_players_data:
            subtracted_list = np.array(player_datum[1:]).astype(np.int64) - np.array(special_voter_vote)
            player_name = player_datum[0]
            output_data.append({
                "name": player_name,
                "point": np.count_nonzero(subtracted_list == 0)
            })
        ranking_df = pd.DataFrame(output_data)
        top_n = ranking_df.sort_values("point", ascending=False).head(n).to_dict("records")
        return top_n
    except Exception as e:
        print(f"Error:{e}")
        return []
out_data = process_data(special_voter=special_voter, data = data, n = 1)

def score_data(vari):
    score = out_data[0][vari]
    return score