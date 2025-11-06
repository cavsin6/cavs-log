import os
import json
import csv

DATA_DIR = "data"
JSON_PATH = os.path.join(DATA_DIR, "games.json")
CSV_PATH = os.path.join(DATA_DIR, "games.csv")

def save_game_data(game_data):
    os.makedirs(DATA_DIR, exist_ok=True)
    _append_to_json(game_data)
    _append_to_csv(game_data)
    print("✅ Game data saved.")

def _append_to_json(game_data):
    try:
        with open(JSON_PATH, " as f:
            games = json.load(f)
    except:
        games = []
    games.append(game_data)
    with open(JSON_PATH, "w") as f:
        json.dump(games, f, indent=2)

def _append_to_csv(game_data):
    row = {
        "Date": game_data["date"],
        "Opponent": game_data["opponent"],
        "Location": game_data["location"],
        "Cavs Score": game_data["cavs_score"],
        "Opponent Score": game_data["opp_score"],
        "Result": game_data["result"],
        "Notes": game_data["notes"]
    }
    for i in range(5):
        if i < len(game_data["players"]):
            p = game_data["players"][i]
            row[f"Player{i+1}_Name"] = p["name"]
            row[f"Player{i+1}_PTS"] = p["points"]
            row[f"Player{i+1}_REB"] = p["rebounds"]
            row[f"Player{i+1}_AST"] = p["assists"]
        else:
            row[f"Player{i+1}_Name"] = ""
            row[f"Player{i+1}_PTS"] = ""
            row[f"Player{i+1}_REB"] = ""
            row[f"Player{i+1}_AST"] = ""
    file_exists = os.path.exists(CSV_PATH)
    with open(CSV_PATH, "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
