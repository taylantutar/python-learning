import json

with open("data.json", "r") as f:
    content = json.load(f)

    for row in content:
        print(f"Color : {row['color']} | Value: {row['value']}")
