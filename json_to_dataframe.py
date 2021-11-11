import pandas as pd
import json
def convert(script, startid):
    character_to_lines = {
        "id": [],
        "character": [],
        "line #": [],
        "line": []
    }
    line_number = 0
    for part in script["movie_script"]:
        if part["type"] == "speech" and "character" in part and  part["character"] != "":
            character_to_lines["line"].append(part["text"])
            character_to_lines["character"].append(part["character"])
            character_to_lines["line #"].append(line_number)
            character_to_lines["id"].append(startid)
            line_number += 1
            startid += 1

    return character_to_lines



f = open('Movies/TheSocialNetwork.json', "r")
 
# Reading from file
data = json.loads(f.read())
line_dict = convert(data, 6140)

line_dict = pd.DataFrame.from_dict(line_dict)

print(line_dict.head())
line_dict.to_csv('Movie_spreadsheets/thesocialnetwork.csv')

