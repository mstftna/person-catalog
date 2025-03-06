import json

def getJsonDataAsDict(path):  
    with open(path, "r") as json_file:       
        data = json.load(json_file)
    return data

def writeDictToJson(path, dictionary):    
    with open(path, 'w') as outfile:         
        return json.dump(dictionary, outfile)