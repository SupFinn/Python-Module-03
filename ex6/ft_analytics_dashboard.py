#!/usr/bin/python3

def main():

    players = {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    }
    sessions = [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
            "Active": True,
            "region": "north",
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "central",
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
            "Active": True,
            "region": "east",
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
            "Active": True,
            "region": "north",
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
            "Active": True,
            "region": "central",
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "east",
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "north",
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
            "Active": True,
            "region": "central",
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
            "Active": True,
            "region": "east",
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "north",
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
            "Active": True,
            "region": "central",
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
            "Active": True,
            "region": "east",
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "north",
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "central",
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
            "Active": True,
            "region": "east",
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
            "Active": True,
            "region": "north",
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
            "Active": True,
            "region": "central",
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
            "Active": True,
            "region": "east",
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
            "Active": True,
            "region": "north",
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "central",
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
            "Active": True,
            "region": "east",
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
            "Active": True,
            "region": "north",
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
            "Active": True,
            "region": "central",
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
            "Active": True,
            "region": "east",
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
            "Active": True,
            "region": "north",
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
            "Active": True,
            "region": "central",
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
            "Active": True,
            "region": "east",
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
            "Active": True,
            "region": "north",
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "central",
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
            "Active": True,
            "region": "east",
        },
    ]
    game_modes = [
        "casual",
        "competitive",
        "ranked"
    ]
    achievements = [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ]

    print("=== Game Analytics Dashboard ===")
    high_scorers = [name for name in players if players[name]['total_score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    doubled_scores = [players[name]['total_score'] * 2 for name in players]
    print(f"Scores doubled: {doubled_scores}")
    active_players = list(set([session['player'] for session in sessions if session['completed']]))
    print(f"Active players: {active_players}")
    print()
    print("=== Dict Comprehension Examples ===")
    player_scores = {name: players[name]['total_score'] for name in players}
    print(f"Player scores: {player_scores}")
    score_categories = {
        "high": len([name for name in players if players[name]['total_score'] > 2000]),
        "medium": len([name for name in players if 1500 <= players[name]['total_score'] <= 2000]),
        "low": len([name for name in players if players[name]['total_score'] < 1500])
    }
    print(f"Score categories: {score_categories}")
    achievement_counts = {name: players[name]['achievements_count'] for name in players}
    print(f"Achievement counts: {achievement_counts}")
    print()
    print(f"=== Set Comprehension Examples ===")
    unique_players = {name for name in players}
    print(f"Unique players {unique_players}")
    unique_achievements = {achievement for achievement in achievements}
    print(f"Unique achievements: {unique_achievements}")  
    active_regions = {session['region'] for session in sessions}
    print(f"Active regions: {active_regions}")
    print()
    print("=== Combined Analysis ===")
    
    total_players = len({player for player in players})
    print(f"Total players: {total_players}")
    total_achievements = len({achievement for achievement in achievements})
    print(f"Total unique achievements: {total_achievements}")
    average_score = sum([players[name]['total_score'] for name in players]) / len(players)
    print(f"Average score: {average_score:.1f}")
    
    player_scores = {name: players[name]['total_score'] for name in players}
    top_player = [name for name in player_scores if player_scores[name] == max(player_scores.values())][0]
    print(f"Top performer: {top_player} ({players[top_player]['total_score']} points, {players[top_player]['achievements_count']} achievements)")


if __name__ == "__main__":
    main()

    
    
# === Game Analytics Dashboard ===

# === List Comprehension Examples ===
# High scorers (>2000): ['alice', 'charlie', 'diana']
# Scores doubled: [4600, 3600, 4300, 4100]
# Active players: ['alice', 'bob', 'charlie']

# === Dict Comprehension Examples ===
# Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}
# Score categories: {'high': 3, 'medium': 2, 'low': 1}
# Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}

# === Set Comprehension Examples ===
# Unique players: {'alice', 'bob', 'charlie', 'diana'}
# Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
# Active regions: {'north', 'east', 'central'}

# === Combined Analysis ===
# Total players: 4
# Total unique achievements: 12
# Average score: 2062.5
# Top performer: alice (2300 points, 5 achievements)