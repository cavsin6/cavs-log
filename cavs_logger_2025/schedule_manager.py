import os
import json

SCHEDULE_PATH = "data/schedule.json"

def get_upcoming_games():
    if not os.path.exists(SCHEDULE_PATH):
        return []
    with open(SCHEDULE_PATH, "r") as f:
        return [g for g in json.load(f) if not g.get("logged", False)]

def mark_game_logged(date, opponent):
    if not os.path.exists(SCHEDULE_PATH):
        return
    with open(SCHEDULE_PATH, "r") as f:
        games = json.load(f)
    for g in games:
        if g["date"] == date and g["opponent"].lower() == opponent.lower():
            g["logged"] = True
    with open(SCHEDULE_PATH, "w") as f:
        json.dump(games, f, indent=2)
