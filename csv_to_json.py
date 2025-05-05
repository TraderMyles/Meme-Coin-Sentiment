import csv
import json

# def csv_to_json(csv_path, json_path):
#     coins = []

#     with open(csv_path, mode='r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             name = row["Meme Coin"]
#             ticker = row["Tickers"]
#             # Split aliases by comma and strip whitespace
#             aliases = [alias.strip() for alias in row["Nicknames"].split(",") if alias.strip()]
            
#             coins.append({
#                 "name": name,
#                 "ticker": ticker,
#                 "aliases": aliases
#             })

#     with open(json_path, mode='w', encoding='utf-8') as file:
#         json.dump(coins, file, indent=4)
#         print(f"✅ JSON saved to {json_path}")

# # Example usage
# csv_to_json("meme_coins.csv", "coins.json")

with open ("meme_coins.csv", "r") as f:
    reader = csv.reader(f)
    next(reader) # Let's you skip header line
    data = {"coins": []}
    for row in reader:
        data["coins"].append({"id": row[0], "name": row[1], "market cap": row[2], "ticker": row[3], "nickname": row[4]})

with open ("meme_coins.json", "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False) # ensure_ascii turns \u2019 -> apostrophe (') 
    