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
              f"({item_data['category']}, {item_data['rarity']}) "
              f"{item_data['quantity']}x @ "
              f"{item_data['value']} gold each = "
              f"{item_data['quantity'] * item_data['value']} gold")
        total_gold += item_data['value'] * item_data['quantity']
        total_quantity += item_data['quantity']

    print(f"Inventory value: {total_gold} gold")
    print(f"Item count: {total_quantity} items")
    print(f"Categories: weapon({alice['sword']['quantity']}), "
          f"consumable({alice['potion']['quantity']}), "
          f"armor({alice['shield']['quantity']})")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    alice['potion']['quantity'].update({"quantity": alice['potion']['quantity'] - 2})
    bob['potion']['quantity'].update({"quantity": bob['potion']['quantity'] + 2})
    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice['potion']['quantity']}")
    print(f"Bob potions: {alice['potion']['quantity']}")

