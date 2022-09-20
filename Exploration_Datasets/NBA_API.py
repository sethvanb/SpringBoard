import requests
import csv

csv_file = open('joelEmbid_data.csv', 'w')
csv_writer = csv.writer(csv_file)

response = requests.get("https://www.balldontlie.io/api/v1/stats?seasons[]=2021&player_ids[]=145&postseason=false&per_page=100")
data = response.json()["data"]
count = 0
for x in data:
    print(x)
    if count == 0:
        header = x.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(x.values())