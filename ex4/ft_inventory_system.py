#!/usr/bin/python3

if __name__ == "__main__":

    print("=== Player Inventory System ===\n")

    alice = {
        "sword": {"category": "weapon",
                    "rarity": "rare",
                      "quantity": 1,
                        "value": 500},

        "potion": {"category": "consumable",
                    "rarity": "common",
                      "quantity": 5,
                        "value": 50},

        "shield": {"category": "armor",
                    "rarity": "uncommon",
                      "quantity": 1,
                        "value": 200}
    }
    bob = {
        "sword": {"category": "weapon",
                    "rarity": "rare",
                      "quantity": 0,
                        "value": 500},

        "potion": {"category": "consumable",
                    "rarity": "common",
                      "quantity": 0,
                        "value": 50},

        "shield": {"category": "armor",
                    "rarity": "uncommon",
                      "quantity": 0,
                        "value": 200}
    }
    

    total_gold = 0
    total_quantity = 0
    print("=== Alice's Inventory ===")
    for item_name, item_data in alice.items():
        print(f"{item_name} "
              f"({item_data.get('category')}, {item_data.get('rarity')}) "
              f"{item_data.get('quantity')}x @ "
              f"{item_data['value']} gold each = "
              f"{item_data.get('quantity') * item_data['value']} gold")
        total_gold += item_data['value'] * item_data.get('quantity')
        total_quantity += item_data.get("quantity")

    print(f"\nInventory value: {total_gold} gold")
    print(f"Item count: {total_quantity} items")
    print(f"Categories: weapon({alice['sword']['quantity']}), "
          f"consumable({alice['potion']['quantity']}), "
          f"armor({alice['shield']['quantity']})")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    alice['potion']['quantity'] -= 2
    bob['potion']['quantity'] += 2
    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion']['quantity']}")
    print(f"Bob potions: {bob['potion']['quantity']}")

    print("\n=== Inventory Analytics ===")
    alice_gold = 0
    for item_data in alice.values():
        alice_gold += item_data["quantity"] * item_data["value"]

    bob_gold = 0
    for item_data in bob.values():
        bob_gold += item_data["quantity"] * item_data["value"]

    if alice_gold > bob_gold:
        print(f"Most valuable player: Alice ({alice_gold} gold)")
    elif bob_gold > alice_gold:
        print(f"Most valuable player: Bob ({bob_gold} gold)")
    else:
        print("Most valuable player: Tie!")

    alice_items = 0
    for item_data in alice.values():
        alice_items += item_data["quantity"]

    bob_items = 0
    for item_data in bob.values():
        bob_items += item_data["quantity"]

    if alice_items > bob_items:
        print(f"Most items: Alice ({alice_items} items)")
    elif bob_items > alice_items:
        print(f"Most items: Bob ({bob_items} items)")
    else:
        print("Most items: Tie!")







# #!/usr/bin/python3

# if __name__ == "__main__":

#     print("=== Player Inventory System ===\n")

#     # Players' inventories
#     alice = {
#         "sword": {"category": "weapon", "rarity": "rare", "quantity": 1, "value": 500},
#         "potion": {"category": "consumable", "rarity": "common", "quantity": 5, "value": 50},
#         "shield": {"category": "armor", "rarity": "uncommon", "quantity": 1, "value": 200}
#     }
#     bob = {
#         "sword": {"category": "weapon", "rarity": "rare", "quantity": 0, "value": 500},
#         "potion": {"category": "consumable", "rarity": "common", "quantity": 0, "value": 50},
#         "shield": {"category": "armor", "rarity": "uncommon", "quantity": 0, "value": 200}
#     }

#     # ------------------------
#     # Print Alice's Inventory
#     # ------------------------
#     total_gold = 0
#     total_quantity = 0
#     print("=== Alice's Inventory ===")
#     for item_name, item_data in alice.items():
#         item_total = item_data.get("quantity") * item_data.get("value")
#         print(f"{item_name} "
#               f"({item_data.get('category')}, {item_data.get('rarity')}): "
#               f"{item_data.get('quantity')}x @ {item_data.get('value')} gold each = {item_total} gold")
#         total_gold += item_total
#         total_quantity += item_data.get("quantity")

#     print(f"\nInventory value: {total_gold} gold")
#     print(f"Item count: {total_quantity} items")
#     print(f"Categories: weapon({alice['sword']['quantity']}), "
#           f"consumable({alice['potion']['quantity']}), "
#           f"armor({alice['shield']['quantity']})")

#     # ------------------------
#     # Transaction
#     # ------------------------
#     print("\n=== Transaction: Alice gives Bob 2 potions ===")
#     alice['potion'].update({"quantity": alice['potion'].get("quantity") - 2})
#     bob['potion'].update({"quantity": bob['potion'].get("quantity") + 2})
#     print("Transaction successful!")

#     print("\n=== Updated Inventories ===")
#     print(f"Alice potions: {alice['potion']['quantity']}")
#     print(f"Bob potions: {bob['potion']['quantity']}")

#     # ------------------------
#     # Inventory Analytics
#     # ------------------------
#     print("\n=== Inventory Analytics ===")

#     # Total gold per player
#     alice_gold = 0
#     alice_items = 0
#     for item_name, item_data in alice.items():
#         alice_gold += item_data.get("quantity") * item_data.get("value")
#         alice_items += item_data.get("quantity")

#     bob_gold = 0
#     bob_items = 0
#     for item_name, item_data in bob.items():
#         bob_gold += item_data.get("quantity") * item_data.get("value")
#         bob_items += item_data.get("quantity")

#     # Most valuable player
#     if alice_gold >= bob_gold:
#         print(f"Most valuable player: Alice ({alice_gold} gold)")
#     else:
#         print(f"Most valuable player: Bob ({bob_gold} gold)")

#     # Player with most items
#     if alice_items >= bob_items:
#         print(f"Most items: Alice ({alice_items} items)")
#     else:
#         print(f"Most items: Bob ({bob_items} items)")

#     # Find rare items across both inventories
#     rare_items = []
#     for player in [alice, bob]:
#         for item_name, item_data in player.items():
#             if item_data.get("rarity") == "rare" and item_data.get("quantity") > 0:
#                 if item_name not in rare_items:
#                     rare_items.append(item_name)
#     print("Rarest items:", end=" ")
#     for i in range(len(rare_items)):
#         print(rare_items[i], end="")
#         if i < len(rare_items) - 1:
#             print(", ", end="")
#     print()
