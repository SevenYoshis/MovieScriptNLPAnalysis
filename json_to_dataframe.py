import pandas as pd
import json
def convert(script):
    character_to_lines = dict()
    characters = set()

    for part in script["movie_script"]:
        if part["type"] == "speech" and part["character"] != "":
            line = part["text"]
            if part["character"] not in characters:
                characters.add(part["character"])
                character_to_lines[part["character"]] = [line]
            else:
                character_to_lines[part["character"]].append(line)

    return character_to_lines

def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if  ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list            



f = open('Movies/Coco.json', "r")
 
# Reading from file
data = json.loads(f.read())
line_dict = convert(data)
line_dict = pad_dict_list(line_dict, " ")
line_dict = pd.DataFrame.from_dict(line_dict)

print(line_dict.head())
line_dict.to_csv('Movie_spreadsheets/coco.csv')

