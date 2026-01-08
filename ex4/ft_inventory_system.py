#!/usr/bin/python3

if __name__ == "__main__":

    print("=== Player Inventory System ===\n")

    # Players and their items
    players = {
        "alice": {
            "sword": {"category": "weapon", "rarity": "rare", "quantity": 1, "value": 500},
            "potion": {"category": "consumable", "rarity": "common", "quantity": 5, "value": 50},
            "shield": {"category": "armor", "rarity": "uncommon", "quantity": 1, "value": 200},
            "magic_ring": {"category": "accessory", "rarity": "legendary", "quantity": 0, "value": 1000}  # added for analytics
        },
        "bob": {
            "sword": {"category": "weapon", "rarity": "rare", "quantity": 0, "value": 500},
            "potion": {"category": "consumable", "rarity": "common", "quantity": 0, "value": 50},
            "shield": {"category": "armor", "rarity": "uncommon", "quantity": 0, "value": 200},
            "magic_ring": {"category": "accessory", "rarity": "legendary", "quantity": 0, "value": 1000}
        }
    }

    # Print Alice's Inventory
    total_gold = 0
    total_quantity = 0
    print("=== Alice's Inventory ===")
    for item_name, item_data in players["alice"].items():
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
    print()





# #!/usr/bin/python3

# if __name__ == "__main__":

#     print("=== Player Inventory System ===\n")

#     alice = {
#         "sword": {"category": "weapon",
#                     "rarity": "rare",
#                       "quantity": 1,
#                         "value": 500},

#         "potion": {"category": "consumable",
#                     "rarity": "common",
#                       "quantity": 5,
#                         "value": 50},

#         "shield": {"category": "armor",
#                     "rarity": "uncommon",
#                       "quantity": 1,
#                         "value": 200}
#     }
#     bob = {
#         "sword": {"category": "weapon",
#                     "rarity": "rare",
#                       "quantity": 0,
#                         "value": 500},

#         "potion": {"category": "consumable",
#                     "rarity": "common",
#                       "quantity": 0,
#                         "value": 50},

#         "shield": {"category": "armor",
#                     "rarity": "uncommon",
#                       "quantity": 0,
#                         "value": 200}
#     }
    

#     total_gold = 0
#     total_quantity = 0
#     print("=== Alice's Inventory ===")
#     for item_name, item_data in alice.items():
#         print(f"{item_name} "
#               f"({item_data.get('category')}, {item_data.get('rarity')}) "
#               f"{item_data.get('quantity')}x @ "
#               f"{item_data.get('value')} gold each = "
#               f"{item_data.get('quantity') * item_data.get('value')} gold")
#         total_gold += item_data.get('value') * item_data.get('quantity')
#         total_quantity += item_data.get("quantity")

#     print(f"\nInventory value: {total_gold} gold")
#     print(f"Item count: {total_quantity} items")
#     print(f"Categories: weapon({alice['sword']['quantity']}), "
#           f"consumable({alice['potion']['quantity']}), "
#           f"armor({alice['shield']['quantity']})")

#     print("\n=== Transaction: Alice gives Bob 2 potions ===")
#     alice['potion']['quantity'] -= 2
#     bob['potion']['quantity'] += 2
#     print("Transaction successful!")

#     print("\n=== Updated Inventories ===")
#     print(f"Alice potions: {alice['potion']['quantity']}")
#     print(f"Bob potions: {bob['potion']['quantity']}")

#     print("\n=== Inventory Analytics ===")
#     alice_gold = 0
#     for item_data in alice.values():
#         alice_gold += item_data["quantity"] * item_data["value"]

#     bob_gold = 0
#     for item_data in bob.values():
#         bob_gold += item_data["quantity"] * item_data["value"]

#     if alice_gold > bob_gold:
#         print(f"Most valuable player: Alice ({alice_gold} gold)")
#     elif bob_gold > alice_gold:
#         print(f"Most valuable player: Bob ({bob_gold} gold)")
#     else:
#         print("Most valuable player: Tie!")

#     alice_items = 0
#     for item_data in alice.values():
#         alice_items += item_data["quantity"]

#     bob_items = 0
#     for item_data in bob.values():
#         bob_items += item_data["quantity"]

#     if alice_items > bob_items:
#         print(f"Most items: Alice ({alice_items} items)")
#     elif bob_items > alice_items:
#         print(f"Most items: Bob ({bob_items} items)")
#     else:
#         print("Most items: Tie!")

#     rarity_rank = {
#     "common": 1,
#     "uncommon": 2,
#     "rare": 3,
#     "legendary": 4
#     }

#     highest_rarity = 0
#     rarest_items = []

#     for item_name, item_data in alice.items():
#         rarity_value = rarity_rank[item_data["rarity"]]

#         if rarity_value > highest_rarity:
#             highest_rarity = rarity_value
#             rarest_items = [item_name]
#         elif rarity_value == highest_rarity:
#             rarest_items.append(item_name)

#     print("Rarest items: ", end="")

#     i = 0
#     for item in rarest_items:
#         print(item, end="")
#         if i < len(rarest_items) - 1:
#             print(", ", end="")
#         i += 1