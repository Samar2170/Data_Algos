import json
import os

def convert_eia_bulk():
    DIR_PATH="Eia_Text/"
    OUTPUT_DIR ="Eia_Json/"
    files =os.listdir(DIR_PATH)
    for a in files:
        f = open(f"{DIR_PATH}{a}")
        
        print(f"opening file {a}")
        
        content = f.read()
        splitcontent=content.splitlines()
        for s in splitcontent:
            df = json.loads(s)
            try:
                fname = df['series_id']
                with open(f"{OUTPUT_DIR}{fname}.json", "w") as f:
                    json.dump(df, f)
                    print(f"saving file {fname}")
            except Exception as e:
                print(str(e))        

convert_eia_bulk()                
