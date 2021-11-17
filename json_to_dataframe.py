import pandas as pd
import json
import os

def convert(script):
    character_to_lines = {
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
            line_number += 1

    return character_to_lines

path_json = 'Movies'
path_csv = 'Movie_spreadsheets'

for filename in sorted(os.listdir(path_json)):
    if filename.endswith('.json'):
        f = open(os.path.join(path_json, filename), "r")
        data = json.loads(f.read())
        line_dict = convert(data)
     
        line_dict = pd.DataFrame.from_dict(line_dict)
        
        out_filename = filename.replace('.json', '.csv')

        # print(line_dict.head())
        line_dict.to_csv(os.path.join(path_csv, out_filename))

