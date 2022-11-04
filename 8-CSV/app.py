import csv

with open("data.csv", "r", encoding="utf-8") as f:
    read_data = csv.reader(f)
    for item in list(read_data)[1:]:
        # print(item)
        print(f"{item[0]} - {item[1]} - {item[2]} - {item[3]}")
