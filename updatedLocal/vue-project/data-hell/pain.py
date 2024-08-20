import requests
import json

# Opening JSON file
f = open('./out.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)

for i in data:
    info = i['caption_text']

    
    prompt = f"Do not return anthing else but the json, return a json of the name, gender (if mentioned, otherwise make a guess off of the name with 1:male 2:female 3:other), major, where they're from, hobbies (as an array), if they're commited or not (1:true, 2:false, 3:not mentioned), and if they're looking for a roomate(as a boolean), music prefrence (as an array), and contact infomation. {info}"

    data = {
        "prompt": prompt,
        "model": "llama3:8b",
        "stream": False
    }
    response = requests.post("http://127.0.0.1:11434/api/generate", json=data, stream=False)
    json_data = json.loads(response.text)

    print(json_data["response"])
    with open("data/"+i['code']+".json", "w+", encoding="utf-8") as f:
        f.write(json_data["response"])