import random
import json
import os

elements = ["Fire", "Ice", "Lightning", "Earth", "Water", "Air", "Darkness", "Light", "Poison", "Chaos"]

all_mobs = {
    "Goblin": {"health": 50, "damage": 10, "element": "Earth"},
    "Orc": {"health": 100, "damage": 20, "element": "Fire"},
    "Dragon": {"health": 200, "damage": 30, "element": "Fire"},
    "Zombie": {"health": 60, "damage": 12, "element": "Darkness"},
    "Skeleton": {"health": 75, "damage": 15, "element": "Darkness"},
    "Troll": {"health": 90, "damage": 18, "element": "Earth"},
    "Giant Spider": {"health": 80, "damage": 14, "element": "Poison"},
    "Witch": {"health": 70, "damage": 16, "element": "Darkness"},
    "Vampire": {"health": 120, "damage": 25, "element": "Darkness"},
    "Lich": {"health": 150, "damage": 28, "element": "Darkness"},
    "Golem": {"health": 180, "damage": 20, "element": "Earth"},
    "Imp": {"health": 40, "damage": 8, "element": "Fire"},
    "Banshee": {"health": 60, "damage": 14, "element": "Darkness"},
    "Griffin": {"health": 100, "damage": 22, "element": "Air"},
    "Gorgon": {"health": 110, "damage": 24, "element": "Earth"},
    "Harpy": {"health": 70, "damage": 15, "element": "Air"},
    "Hydra": {"health": 200, "damage": 30, "element": "Water"},
    "Manticore": {"health": 130, "damage": 25, "element": "Fire"},
    "Minotaur": {"health": 140, "damage": 28, "element": "Earth"},
    "Mummy": {"health": 90, "damage": 20, "element": "Darkness"},
    "Phoenix": {"health": 160, "damage": 30, "element": "Fire"},
    "Giant Rat": {"health": 30, "damage": 6, "element": "Poison"},
    "Djinn": {"health": 80, "damage": 18, "element": "Air"},
    "Kraken": {"health": 200, "damage": 35, "element": "Water"},
    "Wraith": {"health": 70, "damage": 15, "element": "Darkness"},
    "Behemoth": {"health": 250, "damage": 35, "element": "Earth"},
    "Cyclops": {"health": 120, "damage": 22, "element": "Earth"},
    "Wyvern": {"health": 140, "damage": 28, "element": "Fire"},
    "Naga": {"health": 110, "damage": 20, "element": "Water"},
    "Lamia": {"health": 80, "damage": 18, "element": "Darkness"},
    "Dark Knight": {"health": 200, "damage": 30, "element": "Darkness"},
    "Frost Giant": {"health": 200, "damage": 35, "element": "Ice"},
    "Fire Elemental": {"health": 150, "damage": 25, "element": "Fire"},
    "Earth Elemental": {"health": 160, "damage": 28, "element": "Earth"},
    "Water Elemental": {"health": 150, "damage": 22, "element": "Water"},
    "Air Elemental": {"health": 140, "damage": 20, "element": "Air"},
    "Shade": {"health": 80, "damage": 16, "element": "Darkness"},
    "Ghoul": {"health": 90, "damage": 18, "element": "Darkness"},
    "Hellhound": {"health": 120, "damage": 24, "element": "Fire"},
    "Basilisk": {"health": 100, "damage": 20, "element": "Earth"},
    "Reaper": {"health": 130, "damage": 28, "element": "Darkness"},
    "Dire Wolf": {"health": 70, "damage": 14, "element": "Earth"},
    "Shadow Fiend": {"health": 90, "damage": 20, "element": "Darkness"},
    "Roc": {"health": 150, "damage": 30, "element": "Air"},
    "Storm Dragon": {"health": 220, "damage": 35, "element": "Lightning"},
    "Death Knight": {"health": 180, "damage": 30, "element": "Darkness"},
    "Elder Dragon": {"health": 250, "damage": 40, "element": "Fire"},
    "Ancient Golem": {"health": 250, "damage": 35, "element": "Earth"},
    "Specter": {"health": 70, "damage": 15, "element": "Darkness"},
    "Dreadlord": {"health": 160, "damage": 30, "element": "Darkness"},
    "Chaos Beast": {"health": 180, "damage": 35, "element": "Chaos"},
    "Nightmare": {"health": 90, "damage": 20, "element": "Darkness"},
    "Celestial Being": {"health": 250, "damage": 40, "element": "Light"}
}

subclasses = {
    "Warrior": [
        "Knight", "Berserker", "Paladin", "Gladiator", "Crusader", "Warlord", "Vanguard", "Champion", "Sentinel", "Guardian",
        "Dreadnought", "Reaver", "Battlemaster", "Myrmidon", "Templar", "***** Knight", "Stormbringer", "Swordmaster", "Juggernaut",
        "Blackguard", "Ironclad", "Fury", "Death Knight", "Duelist", "Ranger", "Sword Saint", "Samurai", "Lancer", "Ravager",
        "Blood Knight", "Vindicator", "Warmonger", "Gladiator", "Sellsword", "Dreadblade", "Dragonslayer", "Battlelord", "Doombringer",
        "Hellbane", "Stormcaller", "Warlord", "Ashen Knight", "Steel Sentinel", "Bloodrager", "Iron Vanguard", "Oblivion Knight"

    ],
    "Archer": [
        "Ranger", "Sniper", "Hunter", "Marksman", "Bowmaster", "Sharpshooter", "Trapper", "Pathfinder", "Fletcher", "Bounty Hunter",
        "Arbalist", "Shadow Archer", "Crossbow Expert", "Woodsman", "Falconer", "Stalker", "Sharpshooter", "Warden", "Ranger General",
        "Scout", "Bow Sage", "Elemental Archer", "Silvershadow", "Windwalker", "Quickshot", "Death Archer", "Eagle Eye", "Forest Guardian",
        "Shadow Hunter", "Warbow Master", "Moonlight Archer", "Frost Archer", "Swiftstrider", "Trickshot", "Tactical Archer",
        "Spellbound Archer", "Firebrand", "Twilight Archer", "Master Marksman", "Longshot", "Eldritch Archer", "Arcane Archer", "Spectral Archer"

    ],
    "Mage": [
        "Sorcerer", "Elementalist", "Wizard", "Enchanter", "Necromancer", "Warlock", "Pyromancer", "Cryomancer", "Electromancer", "Geomancer",
        "Illusionist", "Mystic", "Chronomancer", "Arcanist", "Diviner", "Spellblade", "Blood Mage", "Invoker", "Runemaster", "Druid",
        "Alchemist", "Summoner", "Shaman", "Elemental Sage", "Storm Mage", "Shadow Mage", "Astral Mage", "Rune Knight", "Mana Wielder",
        "Tempest Mage", "Ethereal Mage", "Witch", "Cultist", "Mage Knight", "Chaos Mage", "Arcane Sage", "Celestial Mage", "Transmuter",
        "Void Mage", "Elder Mage", "Enigma Mage", "Meteor Mage", "Soul Mage", "Glimmer Mage", "Spellbinder", "Mystic Sage", "Frost Mage"

    ]
}

potions = {"Health Potion": 20, "Mana Potion": 25}
weapon_shop = {"Sword": 100, "Bow": 120, "Staff": 150}
armor_shop = {"Leather Armor": 50, "Iron Armor": 80, "Steel Armor": 100}
all_weapons = {
    "Warrior": [
        "Short Sword", "Long Sword", "Great Sword", "Hand Axe", "Battle Axe", "War Axe", "Wooden Mace", "Iron Mace", "Spiked Mace", "Spear",
        "Broadsword", "Claymore", "Warhammer", "Halberd", "Battle Hammer", "Maul", "Glaive", "Pike", "Polearm", "Morning Star",
        "Scimitar", "Kris", "Crescent Blade", "Cutlass", "Bastard Sword", "Flail", "Hand Axe", "Throwing Axe", "Light Mace", "Heavy Mace",
        "War Club", "Greataxe", "Dire Sword", "Dragon Mace", "Heavy Warhammer", "Viking Axe", "Champion's Sword", "Giant's Club", "Stormhammer", "Colossal Axe"
    ],
    "Archer": [
        "Short Bow", "Long Bow", "Crossbow", "Recurve Bow", "Compound Bow", "Longbow", "Blowgun", "Light Crossbow", "Heavy Crossbow", "Composite Bow",
        "War Bow", "Hunting Bow", "Elven Bow", "Magic Bow", "Flaming Bow", "Ice Bow", "Lightning Bow", "Storm Bow", "Shadow Bow", "Silent Bow",
        "Swift Bow", "Ancient Bow", "Ranger's Bow", "Sniper's Bow", "Falcon Bow", "Eagle's Bow", "Celestial Bow", "Tranquil Bow", "Hunter's Crossbow",
        "Wind Bow", "Dragon's Crossbow", "Silver Bow", "Golden Bow", "Emerald Bow", "Elven Longbow", "Hunter's Recurve Bow", "Phantom Bow", "Cursed Bow"
    ],
    "Mage": [
        "Wooden Staff", "Iron Staff", "Mystic Staff", "Fire Staff", "Ice Staff", "Lightning Staff", "Arcane Staff", "Eldritch Staff", "Dark Staff", "Healing Staff",
        "Sorcerer's Staff", "Elemental Staff", "Wizard's Staff", "Enchanter's Rod", "Mystic Wand", "Crystal Rod", "Staff of Power", "Rune Staff", "Celestial Wand", "Arcane Rod",
        "Staff of Wisdom", "Staff of Flames", "Frost Rod", "Staff of Light", "Shadow Wand", "Necromancer's Staff", "Staff of the Elements", "Eldritch Wand", "Celestial Staff", "Wand of Healing",
        "Fire Wand", "Ice Wand", "Lightning Wand", "Staff of the Ancients", "Staff of the Mages", "Ethereal Staff", "Staff of Knowledge", "Wizard's Wand", "Enchanter's Wand", "Staff of Shadows"
    ]
}

base_weapons = {
    "Warrior": [
        "Dragon Slayer Sword", "Excalibur", "Mjolnir", "Giant's Axe", "Meteor Hammer", "Celestial Mace", "Frostbrand Sword", "Flaming Great Sword", "Shadow Warhammer", "Thunderfury",
        "Eclipse Blade", "Doomhammer", "Stormbreaker", "Soulrender", "Voidblade", "Dreadnought Mace", "Inferno Axe", "Bloodthirsty Sword", "Wyrm's Claw", "Seraphim Spear", "Abyssal Club",
        "Hellfire Mace", "Gloomhaven Hammer", "Ironclad Axe", "Meteorite Sword", "Titan's Mace", "Dragonbone Axe", "Celestial Blade", "Infernal Warhammer", "Eldritch Great Sword", "Vortex Spear",
        "Runeblade", "Dragonscale Mace", "Tempest Axe", "Glacial Warhammer", "Raven's Claw", "Phoenix Sword", "Oathkeeper Mace", "Valkyrie's Spear", "Onyx Warhammer", "Celestial Axe"
    ],
    "Archer": [
        "Legendary Bow", "Shadowhunter Crossbow", "Phoenix Bow", "Stormcaller Bow", "Dragon's Eye Bow", "Moonlit Crossbow", "Eagle Eye Bow", "Frostbite Longbow", "Firestorm Crossbow", "Ancient Hunter's Bow",
        "Celestial Crossbow", "Dragon's Fury Bow", "Lightningstrike Bow", "Artemis's Bow", "Shadowstrike Crossbow", "Stormwind Bow", "Sunflare Crossbow", "Emerald Eye Bow", "Spectral Longbow", "Viper's Bow",
        "Shadowstalker Crossbow", "Thunderstrike Longbow", "Windrider's Bow", "Elven Longbow", "Frostfang Bow", "Inferno Crossbow", "Celestial Longbow", "Serpent's Bow", "Moonshadow Crossbow", "Starfire Bow",
        "Stormblade Crossbow", "Dragon's Talon Bow", "Spectral Crossbow", "Sunset Bow", "Venomstrike Longbow", "Frostfire Crossbow", "Celestial Archer's Bow", "Hunter's Mark Bow", "Shadowflame Longbow", "Starlight Bow"
    ],
    "Mage": [
        "Staff of the Archmage", "Firelord's Wand", "Ice Queen's Staff", "Stormcaster's Rod", "Celestial Orb", "Wand of Eternity", "Mystic Wand of Wisdom", "Inferno Staff", "Frostweaver's Rod", "Thunderstrike Wand",
        "Sorcerer's Crystal Staff", "Elemental Scepter", "Eldritch Wand of Power", "Celestial Mage's Staff", "Runewood Wand", "Arcane Orb", "Wand of the Void", "Staff of Eternity", "Firestorm Wand", "Frostfire Staff",
        "Arcane Staff of Wisdom", "Celestial Fire Staff", "Elemental Rod", "Staff of Shadows", "Wand of the Elements", "Infernal Wand", "Crystal Staff of Power", "Wand of Arcana", "Lightning Rod", "Eldritch Staff of Night",
        "Celestial Wand of Light", "Sorcerer's Flame Staff", "Frozen Rod", "Mystic Scepter", "Arcane Crystal Staff", "Wand of Knowledge", "Stormcaller Staff", "Eldritch Crystal Wand", "Frostweaver's Scepter", "Celestial Arcane Staff"
    ]
}

player_class = None
player_subclass = None
items = []
coins = 100
current_area = "Village"
stats = {"level": 1, "health": 100, "mana": 50, "damage": 10, "element": random.choice(elements)}
ego_weapon = None
username = ""

def login():
    global username
    username = input("Enter your username: ")
    print(f"Welcome, {username}!")

def save_game():
    global player_class, items, coins, current_area, stats, player_subclass
    save_data = {
        "username": username,
        "player_class": player_class,
        "player_subclass": player_subclass,
        "items": items,
        "coins": coins,
        "current_area": current_area,
        "stats": stats,
        "ego_weapon": ego_weapon
    }
    with open("save_game.json", "w") as f:
        json.dump(save_data, f, indent=4)
    print("Game saved successfully.")

def load_game():
    global username, player_class, items, coins, current_area, stats, player_subclass, ego_weapon
    if os.path.exists("save_game.json"):
        with open("save_game.json", "r") as f:
            save_data = json.load(f)
        username = save_data["username"]
        player_class = save_data["player_class"]
        player_subclass = save_data["player_subclass"]
        items = save_data["items"]
        coins = save_data["coins"]
        current_area = save_data["current_area"]
        stats = save_data["stats"]
        ego_weapon = save_data.get("ego_weapon", None)
        print(f"Game loaded successfully. Welcome back, {username}!")
    else:
        print("No save file found.")

def choose_class():
    global player_class
    print("Choose your class:")
    print("1. Warrior")
    print("2. Archer")
    print("3. Mage")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        player_class = "Warrior"
    elif choice == "2":
        player_class = "Archer"
    elif choice == "3":
        player_class = "Mage"
    else:
        print("Invalid choice. Defaulting to Warrior.")
        player_class = "Warrior"
    print(f"You are now a {player_class}!")

def class_ability():
    if player_class == "Warrior":
        print("1. Shield Bash\n2. Power Strike\n3. Battle Cry")
    elif player_class == "Archer":
        print("1. Arrow Rain\n2. Eagle Eye\n3. Snare Trap")
    elif player_class == "Mage":
        print("1. Fireball\n2. Ice Shield\n3. Lightning Bolt")
    choice = input("Choose an ability: ")
    return choice

def item_ability():
    print("1. Healing Potion\n2. Mana Potion")
    choice = input("Choose an item: ")
    return choice

def secondary_class_ability():
    if player_subclass == "Paladin":
        print("1. Divine Shield")
    elif player_subclass == "Sniper":
        print("1. Headshot")
    elif player_subclass == "Sorcerer":
        print("1. Meteor Storm")
    choice = input("Choose a secondary ability: ")
    return choice

def encounter_monster(horde=False):
    if current_area == "Village":
        print("You are in a safe zone. No monsters here.")
        return

    if horde:
        print("\nA horde of monsters appears!")
        monsters = random.sample(list(all_mobs.keys()), random.randint(2, 5))
        for mob_name in monsters:
            mob_info = all_mobs[mob_name]
            mob_health = mob_info["health"]
            mob_damage = mob_info["damage"]
            mob_element = mob_info["element"]
            print(f"A wild {mob_name} appears!")
            fight_horde(mob_name, mob_health, mob_damage, mob_element)
    else:
        mob_name = random.choice(list(all_mobs.keys()))
        mob_info = all_mobs[mob_name]
        mob_health = mob_info["health"]
        mob_damage = mob_info["damage"]
        mob_element = mob_info["element"]
        print(f"\nA wild {mob_name} appears!")
        fight_monster(mob_name, mob_health, mob_damage, mob_element)

def fight_horde(mob_name, mob_health, mob_damage, mob_element):
    global stats
    player_health = stats['health']
    
    while mob_health > 0 and player_health > 0:
        print(f"\nFighting {mob_name} (Horde):")
        action = input("Do you want to Attack, Use a Potion, or Use an Ability? (attack/potion/ability): ").lower()
        
        if action == "attack":
            damage = stats['damage'] + random.randint(-5, 5)
            mob_health -= damage
            print(f"You dealt {damage} damage to the {mob_name}.")
        elif action == "potion":
            use_potions()
            continue
        elif action == "ability":
            ability = class_ability()
            print(f"You used ability {ability}!")
        else:
            print("Invalid action. Please choose 'attack', 'potion', or 'ability'.")
            continue
        
        if mob_health <= 0:
            print(f"You have defeated a {mob_name} from the horde!")
            global coins
            coins += 50
            break

        player_health -= mob_damage
        print(f"The {mob_name} dealt {mob_damage} damage to you.")
        
        if player_health <= 0:
            print("You have been defeated!")
            break
    
    stats['health'] = player_health

def fight_monster(mob_name, mob_health, mob_damage, mob_element):
    global stats
    player_health = stats['health']
    
    while mob_health > 0 and player_health > 0:
        print(f"\nFighting {mob_name}:")
        action = input("Do you want to Attack, Use a Potion, or Use an Ability? (attack/potion/ability): ").lower()
        
        if action == "attack":
            damage = stats['damage'] + random.randint(-5, 5)
            mob_health -= damage
            print(f"You dealt {damage} damage to the {mob_name}.")
        elif action == "potion":
            use_potions()
            continue
        elif action == "ability":
            ability = class_ability()
            print(f"You used ability {ability}!")
        else:
            print("Invalid action. Please choose 'attack', 'potion', or 'ability'.")
            continue
        
        if mob_health <= 0:
            print(f"You have defeated the {mob_name}!")
            global coins
            coins += 50
            break

        player_health -= mob_damage
        print(f"The {mob_name} dealt {mob_damage} damage to you.")
        
        if player_health <= 0:
            print("You have been defeated!")
            break
    
    stats['health'] = player_health

def use_potions():
    global coins
    print("\nPotions available:")
    for potion, price in potions.items():
        print(f"{potion}: {price} coins")
    choice = input("Enter the name of the potion you want to use: ")
    if choice in potions:
        if coins >= potions[choice]:
            coins -= potions[choice]
            if choice == "Health Potion":
                stats['health'] += 50
                print(f"You used a {choice}. Your health is now {stats['health']}.")
            elif choice == "Mana Potion":
                stats['mana'] += 50
                print(f"You used a {choice}. Your mana is now {stats['mana']}.")
        else:
            print("Not enough coins.")
    else:
        print("Invalid potion choice.")

def choose_area():
    global current_area
    print("\nWhere do you want to go?")
    print("1. Village")
    print("2. Dungeon")
    print("3. Forest")
    area_choice = input("Enter the number of your choice: ")
    
    if area_choice == "1":
        current_area = "Village"
    elif area_choice == "2":
        current_area = "Dungeon"
    elif area_choice == "3":
        current_area = "Forest"
    else:
        print("Invalid choice. Please choose a valid area.")
        choose_area()
    return current_area

def job_change_quest():
    global player_class, player_subclass
    print("\nYou have encountered a mysterious NPC offering a quest!")
    print("They tell you of an ancient power hidden in the depths of the world, a power that can enhance your abilities.")
    accept_quest = input("Do you accept the quest to unlock a new subclass? (yes/no): ").lower()

    if accept_quest == "yes":
        print(f"\nThe NPC gives you a task: 'To unlock the hidden power, you must collect the three Shards of Light.")
        print("These shards are located in a nearby dungeon, guarded by formidable creatures. Only those who prove their worth will gain the power of a new subclass.'")
        
        print("\nYour journey begins...")

        # Simulating the quest with a simple check. This could be expanded with actual game mechanics.
        shards_collected = 0
        for i in range(3):
            print(f"\nEncounter {i + 1}:")
            result = input("Do you want to fight the guardian of this shard? (yes/no): ").lower()
            if result == "yes":
                print(f"You engage in a fierce battle with {encounter_monster(horde=False)}")
                shards_collected += 1
                print(f"You have collected {shards_collected} Shard(s) of {random.choice(elements)}.")
            else:
                print("You decide not to engage with the guardian.")
                break

        if shards_collected == 3:
            new_subclass = random.choice(subclasses.get(player_class, []))
            print(f"\nCongratulations! After collecting all the Shards of {random.choice(elements)}, the NPC reveals your new subclass: {new_subclass}.")
            player_subclass = new_subclass
        else:
            print(f"\nYou were unable to collect all the Shards of {random.choice(elements)}. The quest remains incomplete.")

    else:
        print("\nYou decline the quest. Perhaps another time...")


def random_event():
    event = random.choice(["Zombie Apocalypse", "Treasure Hunt", "Meteor Shower"])
    if event == "Zombie Apocalypse":
        print("A zombie apocalypse is happening! Zombies are everywhere!")

    elif event == "Treasure Hunt":
        print("A treasure hunt event has started! Find hidden treasures!")

    elif event == "Meteor Shower":
        print("A meteor shower is happening! Some meteors may contain rare items!")

def explore_dungeon():
    print("\nYou have entered a dungeon. You cannot leave until you clear it.")
    floor = 1
    while True:
        print(f"\nYou are on floor {floor}.")
        encounter_monster(horde=random.choice([True, False]))
        action = input("Do you want to continue exploring? (yes/no): ").lower()
        if action == "no":
            print("You cannot leave the dungeon until it is cleared!")
        elif action == "yes":
            floor += 1
            if random.choice([True, False]):
                print(f"A horde of monsters appears on floor {floor}!")
                encounter_monster(horde=True)
        else:
            print("Invalid choice. Please choose 'yes' or 'no'.")

def explore_forest():
    print("\nYou have entered the forest.")
    while True:
        encounter_monster(horde=random.choice([True, False]))
        action = input("Do you want to continue exploring or return to the village? (continue/return): ").lower()
        if action == "return":
            print("Returning to the village.")
            break
        elif action == "continue": 
            if random.choice([True, False]):
                print(f"A horde of monsters appears!")
                encounter_monster(horde=True)
        else:
            print("Invalid choice. Please choose 'continue' or 'return'.")

def explore_village():
    print("\nYou have entered the village.")
    while True:
        event = random.choice(["find_shop", "meet_npc", "find_treasure"])
        
        if event == "find_shop":
            print("\nYou found a shop! Let's see what they have for sale.")
            shop()
        elif event == "meet_npc":
            print("\nYou meet an old villager who offers you a quest.")
            job_change_quest()
        elif event == "find_treasure":
            print("\nYou find a hidden treasure chest!")
            coins_found = random.randint(20, 100)
            print(f"You found {coins_found} coins!")
            global coins
            coins += coins_found
        
        action = input("\nDo you want to continue exploring or return to the village center? (continue/return): ").lower()
        if action == "return":
            print("Returning to the village center.")
            break
        elif action != "continue":
            print("Invalid choice. Please choose 'continue' or 'return'.")

def shop():
    global coins
    if current_area != "Village":
        print("You can only visit the shop while in the village.")
        return

    print("\nWelcome to the shop!")
    print("1. Buy Potions")
    print("2. Buy Weapons")
    print("3. Buy Armor")
    print("4. Visit Blacksmith")
    print("5. Exit Shop")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        use_potions()
    elif choice == "2":
        print("\nWeapons for sale:")
        for weapon, price in weapon_shop.items():
            print(f"{weapon}: {price} coins")
        weapon_choice = input("Enter the name of the weapon you want to buy: ")
        if weapon_choice in weapon_shop:
            if coins >= weapon_shop[weapon_choice]:
                coins -= weapon_shop[weapon_choice]
                items.append(weapon_choice)
                print(f"You bought a {weapon_choice}.")
            else:
                print("Not enough coins.")
        else:
            print("Invalid weapon choice.")
    elif choice == "3":
        print("\nArmor for sale:")
        for armor, price in armor_shop.items():
            print(f"{armor}: {price} coins")
        armor_choice = input("Enter the name of the armor you want to buy: ")
        if armor_choice in armor_shop:
            if coins >= armor_shop[armor_choice]:
                coins -= armor_shop[armor_choice]
                items.append(armor_choice)
                print(f"You bought {armor_choice}.")
            else:
                print("Not enough coins.")
    elif choice == "4":
        visit_blacksmith()
    elif choice == "5":
        print("Exiting shop.")
    else:
        print("Invalid choice. Please try again.")

def visit_blacksmith():
    global coins, items
    print("\nWelcome to the Blacksmith! Here you can buy or craft weapons and armor.")
    print("1. Buy Weapons")
    print("2. Buy Armor")
    print("3. Craft Weapons/Armor")
    print("4. Exit Blacksmith")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("\nWeapons for sale:")
        for weapon, price in weapon_shop.items():
            print(f"{weapon}: {price} coins")
        weapon_choice = input("Enter the name of the weapon you want to buy: ")
        if weapon_choice in weapon_shop:
            if coins >= weapon_shop[weapon_choice]:
                coins -= weapon_shop[weapon_choice]
                items.append(weapon_choice)
                print(f"You bought a {weapon_choice}.")
            else:
                print("Not enough coins.")
        else:
            print("Invalid weapon choice.")
    elif choice == "2":
        print("\nArmor for sale:")
        for armor, price in armor_shop.items():
            print(f"{armor}: {price} coins")
        armor_choice = input("Enter the name of the armor you want to buy: ")
        if armor_choice in armor_shop:
            if coins >= armor_shop[armor_choice]:
                coins -= armor_shop[armor_choice]
                items.append(armor_choice)
                print(f"You bought {armor_choice}.")
            else:
                print("Not enough coins.")
    elif choice == "3":
        craft_items()
    elif choice == "4":
        print("Exiting blacksmith.")
    else:
        print("Invalid choice. Please try again.")

def craft_items():
    global coins, items
    print("\nCrafting at the Blacksmith!")
    item_type = input("Do you want to craft a weapon or armor? (weapon/armor): ").lower()
    if item_type not in ["weapon", "armor"]:
        print("Invalid choice. Returning to Blacksmith menu.")
        return
    
    base_cost = 100 if item_type == "weapon" else 80
    max_cost = base_cost * 3
    print(f"The cost to craft an item ranges from {base_cost} to {max_cost} coins.")
    amount = int(input("Enter the amount of coins you want to spend: "))

    if amount < base_cost:
        print("Not enough coins to craft an item.")
        return
    elif amount > coins:
        print("You don't have enough coins.")
        return

    quality = "basic"
    if amount > base_cost * 2:
        quality = "superior"
    elif amount > base_cost:
        quality = "enhanced"

    coins -= amount
    if item_type == "weapon":
        damage = random.randint(10, 30) + (amount // 10)
        item = f"{quality} {item_type} with {damage} damage"
    else:
        defense = random.randint(5, 20) + (amount // 10)
        item = f"{quality} {item_type} with {defense} defense"

    items.append(item)
    print(f"You crafted a {item}.")

def main_game_loop():
    login()
    load_game()
    choose_class()
    while True:
        print("\nWhat would you like to do?")
        print("1. Explore Area")
        print("2. Visit Shop")
        print("3. View Stats")
        print("4. Random Event")
        print("5. Save Game")
        print("6. Quit")
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            current_area = choose_area()
            if current_area == "Dungeon":
                explore_dungeon()
            elif current_area == "Forest":
                explore_forest()
            elif current_area == "Village":
                explore_village()
        elif choice == "2":
            shop()
        elif choice == "3":
            print(f"\nPlayer Stats:")
            print(f"Username: {username}")
            print(f"Class: {player_class}")
            print(f"Subclass: {player_subclass}")
            print(f"Level: {stats['level']}")
            print(f"Health: {stats['health']}")
            print(f"Mana: {stats['mana']}")
            print(f"Damage: {stats['damage']}")
            print(f"Element: {stats['element']}")
            print(f"Coins: {coins}")
            print(f"Items: {items}")
            print(f"Ego Weapon: {ego_weapon}")
        elif choice == "4":
            random_event()
        elif choice == "5":
            save_game()
        elif choice == "6":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_game_loop()
