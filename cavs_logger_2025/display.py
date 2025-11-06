import os
import json
from tabulate import tabulate

def show_season_summary():
    from modules.logger import JSON_PATH
    if not os.path.exists(JSON_PATH):
        print("No games logged.")
        return
    with open(JSON_PATH, "r") as f:
        games = json.load(f)
    wins = sum(1 for g in games if g["result"] == "Win")
    losses = len(games) - wins
    print(f"Games: {len(games)}, Wins: {wins}, Losses: {losses}")
    table = [[g["date"], g["opponent"], g["cavs_score"], g["opp_score"], g["result"]] for g in games]
    print(tabulate(table, headers=["Date", "Opponent", "Cavs", "Opp", "Result"]))
