#!/usr/bin/python3

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}
    
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {alice.union(bob, charlie)}")
    print(f"Total unique achievements: {len(alice.union(bob, charlie))}")

    print(f"\nCommon to all players: {alice.intersection(bob, charlie)}")
    alice_unique = alice.difference(bob, charlie)
    bob_unique = bob.difference(alice, charlie)
    charlie_unique = charlie.difference(alice, bob)
    rare_achievements = alice_unique.union(bob_unique, charlie_unique)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")