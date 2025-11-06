from datetime import datetime
from modules.schedule_manager import get_upcoming_games

def get_game_input():
    upcoming = get_upcoming_games()
    if upcoming:
        print("Upcoming Games:")
        for i, game in enumerate(upcoming, 1):
            print(f"{i}. {game['date']} vs {game['opponent']} ({game['location']})")
        choice = input("Select game to log or press Enter for manual: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(upcoming):
            selected = upcoming[int(choice)-1]
            date = selected["date"]
            opponent = selected["opponent"]
            location = selected["location"]
        else:
            date = input("Game date (YYYY-MM-DD): ")
            opponent = input("Opponent: ")
            location = input("Location (Home/Away): ")
    else:
        date = input("Game date (YYYY-MM-DD): ")
        opponent = input("Opponent: ")
        location = input("Location (Home/Away): ")

    cavs_score = int(input("Cavs score: "))
    opp_score = int(input("Opponent score: "))
    result = "Win" if cavs_score > opp_score else "Loss"

    players = []
    for i in range(5):
        name = input(f"Player {i+1} name (leave blank to stop): ")
        if not name:
            break
        pts = int(input("Points: "))
        reb = int(input("Rebounds: "))
        ast = int(input("Assists: "))
        players.append({
            "name": name, "points": pts, "rebounds": reb, "assists": ast
        })

    notes = input("Game notes: ")

    return {
        "date": date,
        "opponent": opponent,
        "location": location,
        "cavs_score": cavs_score,
        "opp_score": opp_score,
        "result": result,
        "players": players,
        "notes": notes
    }
