import os
from datetime import datetime
import json

if __name__ == "__main__":
    lines = []
    linepustaya = False
    while True:
        line = input()
        if line == "":
            if linepustaya:
                break
            else:
                linepustaya = True
    
        lines.append(line)

    text = "\n".join(lines)
    print(text)
    dates = []
    from datetime import datetime, date

    for i in json.loads(text):
        d = i['date']
        v = i['count']

        parsed_date = d
        parsed_date += " 12:00:00"

    
        for _ in range(v):
            os.system(rf'git commit --date="{parsed_date}" -m "not shit"')