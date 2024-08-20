import json
import os
invalid_json_files = []
read_json_files = []
listofthings = {}
def parse():
    for files in os.listdir(os.getcwd()+"/data"):
        with open("data/"+files) as json_file:
            try:
                jsond = json.load(json_file)
                for key in jsond:
                    listofthings.setdefault(key, 0)
                    listofthings[key] += 1
                    # listofthings.setdefault(key+" JSI", [])
                    # listofthings[key+" JSI"].append(files)
            except ValueError:
                print("errrorr")
            
    for key in sorted(listofthings, key=listofthings.get, reverse=True):
        print(key+":"+str(listofthings[key]))
    # for key in listofthings:
    #     print(key+":", end="")
    #     match listofthings[key]:
    #         case list():
    #             if len(listofthings[key]) > 10:
    #                 print("big")
    #             else:
    #                 print(listofthings[key])
    #         case _:
    #             print(listofthings[key])


while True:
    parse()
    listofthings = {}
    fo = input("from:")
    t = input("To:")
    import json
    for files in os.listdir(os.getcwd()+"/data"):
        with open('data/'+files, 'r+') as f:
            try:
                data = json.load(f)
                if fo in data:
                    data[t] = data[fo]
                    del data[fo]
                    f.seek(0)        # <--- should reset file position to the beginning.
                    json.dump(data, f, indent=4)
                    f.truncate() 
            except:
                print("erro")