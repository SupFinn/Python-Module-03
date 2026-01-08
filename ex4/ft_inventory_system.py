#!/usr/bin/python3

if __name__ == "__main__":

    print("=== Player Inventory System ===\n")

    # Players and their items
    players = {
        "alice": {
            "sword": {"category": "weapon", "rarity": "rare", "quantity": 1, "value": 500},
            "potion": {"category": "consumable", "rarity": "common", "quantity": 5, "value": 50},
            "shield": {"category": "armor", "rarity": "uncommon", "quantity": 1, "value": 200},
            "magic_ring": {"category": "accessory", "rarity": "rare", "quantity": 0, "value": 1000}
        },
        "bob": {
            "sword": {"category": "weapon", "rarity": "rare", "quantity": 0, "value": 500},
            "potion": {"category": "consumable", "rarity": "common", "quantity": 0, "value": 50},
            "shield": {"category": "armor", "rarity": "uncommon", "quantity": 0, "value": 200},
            "magic_ring": {"category": "accessory", "rarity": "rare", "quantity": 0, "value": 1000}
        }
    }


    # Print Alice's Inventory
    total_gold = 0
    total_quantity = 0
    print("=== Alice's Inventory ===")
    for item_name, item_data in players["alice"].items():
        if item_data['quantity'] > 0:
            print(f"{item_name} ({item_data['category']}, {item_data['rarity']}): "
                f"{item_data['quantity']}x @ {item_data['value']} gold each = "
                f"{item_data['quantity'] * item_data['value']} gold")
            total_gold += item_data['quantity'] * item_data['value']
            total_quantity += item_data['quantity']

    print(f"\nInventory value: {total_gold} gold")
    print(f"Item count: {total_quantity} items")

    # Count categories dynamically
    category_count = {}
    for item_name, item_data in players["alice"].items():
        if item_data['quantity'] > 0:
            cat = item_data['category']
            category_count[cat] = category_count.get(cat, 0) + item_data['quantity']

    i = 0
    print("Categories: ", end="")
    for cat, count in category_count.items():
        print(f"{cat}({count})", end="")
        if i < len(category_count) - 1:
            print(", ", end="")
        i += 1
    print()

    # Transaction: Alice gives Bob 2 potions
    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    players["alice"]["potion"]["quantity"] -= 2
    players["bob"]["potion"]["quantity"] += 2
    print("Transaction successful!\n")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {players['alice']['potion']['quantity']}")
    print(f"Bob potions: {players['bob']['potion']['quantity']}")

    # Inventory Analytics
    print("\n=== Inventory Analytics ===")

    # Most valuable player
    most_valuable = ""
    highest_gold = 0
    for player_name, player_data in players.items():
        total = 0
        for item_data in player_data.values():
            total += item_data["quantity"] * item_data["value"]
        if total > highest_gold:
            highest_gold = total
            most_valuable = player_name
    print(f"Most valuable player: {most_valuable.capitalize()} ({highest_gold} gold)")

    # Most items
    most_items_player = ""
    highest_items = 0
    for player_name, player_data in players.items():
        total_items = sum(item_data["quantity"] for item_data in player_data.values())
        if total_items > highest_items:
            highest_items = total_items
            most_items_player = player_name
    print(f"Most items: {most_items_player.capitalize()} ({highest_items} items)")

    # Rarest items
    rarity_rank = {"common": 1, "uncommon": 2, "rare": 3, "legendary": 4}
    highest_rarity = 0
    rarest_items = []

    # Check all items from all players
    for player_data in players.values():
        for item_name, item_data in player_data.items():
            rank = rarity_rank[item_data["rarity"]]
            if rank > highest_rarity:
                highest_rarity = rank
                rarest_items = [item_name]
            elif rank == highest_rarity and item_name not in rarest_items:
                rarest_items.append(item_name)

    # Print rarest items
    print("Rarest items: ", end="")
    for i, item in enumerate(rarest_items):
        print(item, end="")
        if i < len(rarest_items) - 1:
            print(", ", end="")
