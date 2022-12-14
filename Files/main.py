# Outside
import sys
import time
import random

# Files
import extras
import extras.save
import extras.skills
import extras.storage
import extras.enemies.tier1
import extras.enemies.tier2
import extras.enemies.tier3
import extras.enemies.tier4
import extras.enemies.tier5

# Variables
file = extras.save
skillz = extras.skills
health = file.health
max_health = file.max_health
strength = file.strength
defense = file.defense
gold = file.gold
armour = file.armour
weapon = file.weapon
xp = file.xp
skillpoints = file.skillpoints
w = skillz.w
a = skillz.a
x = None
difficulty = file.difficulty
storage_ = extras.storage.storage

# Enemies and their vars
enemy_t1 = extras.enemies.tier1
enemy_t2 = extras.enemies.tier2
enemy_t3 = extras.enemies.tier3
enemy_t4 = extras.enemies.tier4
enemy_t5 = extras.enemies.tier5

# Functions

def save():
    file_open = open(file="extras\\save.py", mode="w")
    skillz_open = open(file="extras\\skills.py", mode="w")
    storage_open = open(file="extras\\storage.py", mode="w")
    file_open.write("health = " + str(health) + "\n" + "max_health = " + str(max_health) + "\n" + "strength = " + str(strength) + "\n" + "defense = " + str(defense) + "\n" + "gold = " + str(gold) + "\n" + "armour = " + str(str(armour)) + " " + "\n" + "weapon = " + str(str(weapon)) + " " + "\n" + "xp = " + str(xp) + " " + "\n" + "skillpoints = " + str(skillpoints) + " " + "\ndifficulty = " + str(difficulty) + " \n")
    skillz_open.write("a = " + str(a) + " " + "\n" + "w = " + str(w) + " " + "\n")
    storage_open.write("a_storage = " + str(storage_[0]) + "\nw_storage = " + str(storage_[1]) + "\nstorage = " + str([storage_[0], storage_[1]]) + "\n")

def save_and_exit():
    file_open = open(file="extras\\save.py", mode="w")
    skillz_open = open(file="extras\\skills.py", mode="w")
    storage_open = open(file="extras\\storage.py", mode="w")
    file_open.write("health = " + str(health) + "\n" + "max_health = " + str(max_health) + "\n" + "strength = " + str(strength) + "\n" + "defense = " + str(defense) + "\n" + "gold = " + str(gold) + "\n" + "armour = " + str(str(armour)) + " " + "\n" + "weapon = " + str(str(weapon)) + " " + "\n" + "xp = " + str(xp) + " " + "\n" + "skillpoints = " + str(skillpoints) + " " + "\ndifficulty = " + str(difficulty) + " \n")
    skillz_open.write("a = " + str(a) + " " + "\n" + "w = " + str(w) + " " + "\n")
    storage_open.write("a_storage = " + str(storage_[0]) + "\nw_storage = " + str(storage_[1]) + "\nstorage = " + str([storage_[0], storage_[1]]) + "\n")
    sys.exit()

# Combat System
def Fight(enemy,ph,pmh,ps,pd,pg,pa,pw,px,diffi = 1):
    e_health = enemy.e_health * diffi
    e_strength = enemy.e_strength * diffi
    e_defense = enemy.e_defense * diffi
    e_possibleweapons = enemy.e_possibleweapons
    e_possiblearmour = enemy.e_possiblearmour
    e_tier = enemy.e_tier

    while(ph > 0 and e_health > 0):
        while(e_strength<=pd):
            e_strength = e_strength + 1
        while(ps<=e_defense):
            e_defense = e_defense - 1

        e_health = e_health - (ps-e_defense)
        dmg = ps-e_defense
        print("You damaged the enemy for " + str(dmg) + ".\n" + "He has " + str(e_health) + " remaining.")
        time.sleep(2)
        ph = ph - (e_strength - pd)
        p_dmg = e_strength - pd
        print("The enemy damaged you for " + str(p_dmg) + ".\n" + "You have " + str(ph) + " remaining.")
        time.sleep(2)
        print("\n")

    if(ph <= 0):
        time.sleep(1)
        pg = pg/10
        original_g_a = pg*10
        loss_i_g = original_g_a - pg
        print("You died and lost " + str(loss_i_g) + "g!\n" + "You have " + str(pg) + "g remaining!")
        ph = pmh
    elif(e_health <= 0):
        time.sleep(1)
        pg = pg + (100 * e_tier) * diffi
        print("You have been healed!")
        ph = pmh
        px = px + e_tier * 100 * diffi
        print("You gained " + str(e_tier * 100) + " xp. You have " + str(px) + " total!")
        w1 = e_possibleweapons[0]
        w1_c = int(random.randint(1,int(e_possibleweapons[1])))
        w2 = e_possibleweapons[2]
        w2_c = int(random.randint(1,int(e_possibleweapons[3])))
        a1 = e_possiblearmour[0]
        a1_c = int(random.randint(1,int(e_possiblearmour[1])))
        a2 = e_possiblearmour[2]
        a2_c = int(random.randint(1,int(e_possiblearmour[3])))

        if(w1_c == 1):
            yon_1 = input("Do you want to replace your weapon " + str(pw) + " with " + str(w1) + "? (yes,no) ---> ")
            if(yon_1 == "yes"):
                ps = ps - pw
                pw = w1
                ps = ps + w1
                print("You got your new weapon! Sending back to lobby...")
            elif(yon_1 == "no"):
                print("Ok, sending back to lobby...")
            else:
                print("Not a valid option! Sending back to lobby...")
        elif(w2_c == 1):
            yon_2 = input("Do you want to replace your weapon " + str(pw) + " with " + str(w2) + "? (yes,no) ---> ")
            if(yon_2 == "yes"):
                ps = ps - pw
                pw = w2
                ps = ps + w2
                print("You got your new weapon! Sending back to lobby...")
            elif(yon_2 == "no"):
                print("Ok, sending back to lobby...")
            else:
                print("Not a valid option! Sending back to lobby...")
        else:
            print("You didnt drop any weapons")

        if(a1_c == 1):
            yon_1 = input("Do you want to replace your armour " + str(pa) + " with " + str(a1) + "? (yes,no) ---> ")
            if(yon_1 == "yes"):
                pd = pd - pa
                pa = a1
                pd = pd + a1
                print("You got your new armour! Sending back to lobby...")
            elif(yon_1 == "no"):
                print("Ok, sending back to lobby...")
            else:
                print("Not a valid option! Sending back to lobby...")
        elif(a2_c == 1):
            yon_2 = input("Do you want to replace your armour " + str(pa) + " with " + str(a2) + "? (yes,no) ---> ")
            if(yon_2 == "yes"):
                pd = pd - pa
                pa = a2
                pd = pd + a2
                print("You got your new weapon! Sending back to lobby...")
            elif(yon_2 == "no"):
                print("Ok, sending back to lobby...")
            else:
                print("Not a valid option! Sending back to lobby...")
        else:
            print("You didnt drop any armour")
    return [pg, pw, pa, ps, pd, ph, px]

# Skill System
def SkillAdd(psp,a,w,ps,pd):
    user_wanted_skill = input("What skill do you want to skill? (A,W) ---> ")
    if(user_wanted_skill == "W"):
        if(psp >= 1):
             if(w[6] <= 5):
                psp = psp - 1
                w.pop(w[6])
                w.insert(w[5],"+")
                ps = ps + w[6]
                w[6] = w[6] + 1
                print("Strength skilled!")
             else:
                print("The skill is already maxed!")
        else:
            print("You dont have enough skillpoints to skill Skills!")
    elif(user_wanted_skill == "A"):
        if(psp >= 1):
             if(a[6] <= 5):
                psp = psp - 1
                a.pop(a[6])
                a.insert(a[5],"+")
                pd = pd + a[6]
                a[6] = a[6] + 1
                print("Defense skilled!")
             else:
                print("The skill is already maxed!")
        else:
            print("You dont have enough skillpoints to skill Skills!")
    else:
        print("Wrong Input ---> " + user_wanted_skill)
    return [a, w, ps, pd, psp]

# Storage System
def stor(pa, pw, ps, pd, action: str, item: str, _storage = extras.storage.storage, _a_storage = extras.storage.storage[0], _w_storage = extras.storage.storage[1]):
    i = 0
    allowed_numbers = []
    if(action == "store"):
        if(item == "armour"):
            if(pa == None or pa == 0):
                print("You dont have any armour right now.")
            else:
                _a_storage.insert(len(_a_storage),pa)
                pd = pd - pa
                pa = 0
        elif(item == "weapon"):
            if(pw == None or pw == 0):
                print("You dont have a weapon right now.")
            else:
                _w_storage.insert(len(_w_storage),pw)
                ps = ps - pw
                pw = 0
    elif(action == "take"):
        if(_a_storage == [] and _w_storage == []):
            print("You dont have anything in storage")
        else:
            if(item == "weapon"):
                if(_w_storage == [] or _w_storage == None): return print("You dont have any weapons in storage right now!")
                if(pw == 0):
                    while i < len(_w_storage):
                        i = i + 1
                        allowed_numbers.insert(len(allowed_numbers),i)
                        print(str(i-1) + " = " + str(_w_storage[i-1]))
                    user = int(input("What do you want to take? ---> "))
                    if(user in allowed_numbers):
                        pw = _w_storage[user]
                        _w_storage.remove(_w_storage[user])
                        ps = ps + pw
                    else:
                        print(str(i+1) + " is not a valid pick!")
                else:
                    print("Sorry, but you already have a weapon!")
            elif(item == "armour"):
                if (_a_storage == [] or _a_storage == None): return print("You dont have any armour in storage right now!")
                if(pa == 0):
                    while i < len(_a_storage):
                        i = i + 1
                        allowed_numbers.insert(len(allowed_numbers),i)
                        print(str(i-1) + " = " + str(_a_storage[i-1]))
                    user = int(input("What do you want to take? ---> "))
                    if(user in allowed_numbers):
                        pa = _a_storage[user]
                        _a_storage.remove(_a_storage[user])
                        pd = pd + pa
                    else:
                        print(str(i+1) + " is not a valid pick!")
                else:
                    print("Sorry, but you already have armour!")
    else:
        print("Wrong Input ---> " + str(action))
    return [_storage, pa, pw, pd, ps]

# Shop System
def Shop(gold, strength, armour, defense, weapon):
    print("Shop:\n")
    print("+1 Strength for 1000g (A)")
    print("+1 Defense for 1000g (B)")
    print("Weapon 1 for 100g (C)")
    print("Weapon 5 for 2000g (D)")
    print("Armour 1 for 100g (E)")
    print("Armour 5 for 2000g (F)")
    print("Weapon 10 for 5000g (G)")
    print("Weapon 20 for 10000g (H)")
    print("Armour 10 for 5000g (I)")
    print("Armour 20 for 10000g (J)")
    print("Weapon 50 for 20000g (K)")
    print("Weapon 100 for 50000g (L)")
    print("Armour 50 for 20000g (M)")
    print("Armour 100 for 50000g (N)")
    print("Later Weapons and Armour might come later")

    user_wanted_buy = input("What do you want to buy? (A,B,C,etc) ---> ")

    if(user_wanted_buy == "A"):
        if (gold >= 1000):
            gold = gold - 1000
            strength = strength + 1
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 1000 required!")
    elif (user_wanted_buy == "B"):
        if (gold >= 1000):
            gold = gold - 1000
            defense = defense + 1
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 1000 required!")
    elif (user_wanted_buy == "C"):
        if (gold >= 100):
            gold = gold - 100
            strength = strength - weapon
            weapon = 1
            strength = strength + weapon
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 100 required!")
    elif (user_wanted_buy == "D"):
        if (gold >= 2000):
            gold = gold - 2000
            strength = strength - weapon
            weapon = 5
            strength = strength + weapon
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 2000 required!")
    elif (user_wanted_buy == "E"):
        if (gold >= 100):
            gold = gold - 100
            defense = defense - armour
            armour = 1
            defense = defense + armour
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 100 required!")
    elif (user_wanted_buy == "F"):
        if (gold >= 2000):
            gold = gold - 2000
            defense = defense - armour
            armour = 5
            defense = defense + armour
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 2000 required!")
    elif (user_wanted_buy == "G"):
        if (gold >= 5000):
            gold = gold - 5000
            strength = strength - weapon
            weapon = 10
            strength = strength + weapon
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 5000 required!")
    elif (user_wanted_buy == "H"):
        if (gold >= 10000):
            gold = gold - 10000
            strength = strength - weapon
            weapon = 20
            strength = strength + weapon
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 10000 required!")
    elif (user_wanted_buy == "I"):
        if (gold >= 5000):
            gold = gold - 5000
            defense = defense - armour
            armour = 10
            defense = defense + armour
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 5000 required!")
    elif (user_wanted_buy == "J"):
        if (gold >= 10000):
            gold = gold - 10000
            defense = defense - armour
            armour = 20
            defense = defense + armour
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 10000 required!")
    elif (user_wanted_buy == "K"):
        if (gold >= 20000):
            gold = gold - 20000
            strength = strength - weapon
            weapon = 50
            strength = strength + weapon
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 20000 required!")
    elif (user_wanted_buy == "L"):
        if (gold >= 50000):
            gold = gold - 50000
            strength = strength - weapon
            weapon = 100
            strength = strength + weapon
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 50000 required!")
    elif (user_wanted_buy == "M"):
        if (gold >= 20000):
            gold = gold - 20000
            defense = defense - armour
            armour = 50
            defense = defense + armour
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 20000 required!")
    elif (user_wanted_buy == "N"):
        if (gold >= 50000):
            gold = gold - 50000
            defense = defense - armour
            armour = 100
            defense = defense + armour
            print("Purchase successful!")
        else:
            print("You dont have enough gold! 50000 required!")
    else:
        print("Wrong Input! ---> " + user_wanted_buy)
    return [gold, strength, armour, defense, weapon]


# GameLoop
while(True):
    time.sleep(0.1)
    # Death
    if(health <= 0):
        gold = gold/10
        original_g_a = gold*10
        loss_i_g = original_g_a - gold
        print("You died and lost " + str(loss_i_g) + "g!\n" + "You have " + str(gold) + "g remaining!")
        health = max_health

    if(xp >= 1000):
        xp = xp - 1000
        skillpoints = skillpoints + 1
        print("You just leveled up and gained a skillpoint! You have " + str(skillpoints) + " in total!")

    user_action = input("What do you want to do? (exit,fight,stats,shop,skills,about,storage,log,reset,difficulty) ---> ")
    # Exit and save
    if(user_action == "exit"):
        save_and_exit()
    elif(user_action == "stats"):
        print("health = " + str(health) + "\n" + "max_health = " + str(max_health) + "\n" + "strength = " + str(strength) + "\n" + "defense = " + str(defense) + "\n" + "gold = " + str(gold) + "g\n" + "armour = " + str(armour) + " " + "\n" + "weapon = " + str(weapon) + " " + "\n" + "xp = " + str(xp) + " " + "\n" + "skillpoints = " + str(skillpoints) + " " + "\n")
        print("a = " + str(a) + " " + "\n" + "w = " + str(w) + " " + "\n")
    elif(user_action == "fight"):
        user_wanted_fight = input("What tier do you want to fight? (1,2,3,4,5) ---> ")
        if(user_wanted_fight == "1"):
            x = Fight(enemy=enemy_t1,ph=health,pmh=max_health,ps=strength,pd=defense,pg=gold,pa=armour,pw=weapon,px=xp,diffi=difficulty)
            gold = x[0]
            weapon = x[1]
            armour = x[2]
            strength = x[3]
            defense = x[4]
            health = x[5]
            xp = x[6]
        elif(user_wanted_fight == "2"):
            x = Fight(enemy=enemy_t2,ph=health,pmh=max_health,ps=strength,pd=defense,pg=gold,pa=armour,pw=weapon,px=xp,diffi=difficulty)
            gold = x[0]
            weapon = x[1]
            armour = x[2]
            strength = x[3]
            defense = x[4]
            health = x[5]
            xp = x[6]
        elif(user_wanted_fight == "3"):
            x = Fight(enemy=enemy_t3,ph=health,pmh=max_health,ps=strength,pd=defense,pg=gold,pa=armour,pw=weapon,px=xp,diffi=difficulty)
            gold = x[0]
            weapon = x[1]
            armour = x[2]
            strength = x[3]
            defense = x[4]
            health = x[5]
            xp = x[6]
        elif(user_wanted_fight == "4"):
            x = Fight(enemy=enemy_t4, ph=health, pmh=max_health, ps=strength, pd=defense, pg=gold, pa=armour, pw=weapon,px=xp,diffi=difficulty)
            gold = x[0]
            weapon = x[1]
            armour = x[2]
            strength = x[3]
            defense = x[4]
            health = x[5]
            xp = x[6]
        elif(user_wanted_fight == "5"):
            x = Fight(enemy=enemy_t5, ph=health, pmh=max_health, ps=strength, pd=defense, pg=gold, pa=armour, pw=weapon,px=xp,diffi=difficulty)
            gold = x[0]
            weapon = x[1]
            armour = x[2]
            strength = x[3]
            defense = x[4]
            health = x[5]
            xp = x[6]

    elif(user_action == "shop"):
        x = Shop(gold,strength,armour,defense,weapon)
        gold = x[0]
        strength = x[1]
        armour = x[2]
        defense = x[3]
        weapon = x[4]

    elif(user_action == "skills"):
        x = SkillAdd(psp=skillpoints,a=a,w=w,ps=strength,pd=defense)
        strength = x[2]
        defense = x[3]
        skillpoints = x[4]
        a = x[0]
        w = x[1]

    elif(user_action == "about"):
        print("Game was made by Codex!")
        print("Follow my yt if you want!")
        print("https://www.youtube.com/channel/UCME-adZK2Rqb4mToqqSqApQ")
        print("Version: 1.4")
    elif(user_action == "storage"):
        user_wanted_storage = input("What do you want to do? (store weapon, store armour, take weapon, take armour) -> ")
        if(user_wanted_storage == "store weapon"):
            x = stor(pa=armour,pw=weapon,ps=strength,pd=defense,action="store",item="weapon")
            storage_ = x[0]
            armour = x[1]
            weapon = x[2]
            defense = x[3]
            strength = x[4]
        elif(user_wanted_storage == "store armour"):
            x = stor(pa=armour, pw=weapon, ps=strength, pd=defense, action="store", item="armour")
            storage_ = x[0]
            armour = x[1]
            weapon = x[2]
            defense = x[3]
            strength = x[4]
        elif(user_wanted_storage == "take weapon"):
            x = stor(pa=armour, pw=weapon, ps=strength, pd=defense, action="take", item="weapon")
            storage_ = x[0]
            armour = x[1]
            weapon = x[2]
            defense = x[3]
            strength = x[4]
        elif(user_wanted_storage == "take armour"):
            x = stor(pa=armour, pw=weapon, ps=strength, pd=defense, action="take", item="armour")
            storage_ = x[0]
            armour = x[1]
            weapon = x[2]
            defense = x[3]
            strength = x[4]
        else:
            print("Wrong Input ---> " + str(user_wanted_storage))
    elif (user_action == "log"):
        print("1.0: First Version of the game! \n1.1: Added Storage function and this log!")
        print("1.2: Fixed Bugs with storage system and added the reset function!")
        print("1.3: Made the Shop into a function!")
        print("1.4: Added the difficulty feature and made save and save_and_exit into a function for bigger use also moved to README.txt file!")
    elif(user_action == "reset"):
        user_wanted_reset = input("Do you really wanna reset? (Storage doesnt reset!) (y) ---> ")
        if(user_wanted_reset == "y"):
            health = 100
            max_health = 100
            strength = 1
            defense = 1
            gold = 0
            armour = 0
            weapon = 0
            xp = 0
            skillpoints = 0
            a = ['-', '-', '-', '-', '-', '-', 0]
            w = ['-', '-', '-', '-', '-', '-', 0]
            save()
    elif(user_action == "difficulty"):
        print("Current Difficulty: " + str(difficulty))
        user_difficulty = input("Whats the difficulty you want to set? (1 is default!) (1,1.1,1.3,1.7,2) ---> ")
        if(user_difficulty == "1"):
            difficulty = 1
        elif(user_difficulty == "1.1"):
            difficulty = 1.1
        elif(user_difficulty == "1.3"):
            difficulty = 1.3
        elif(user_difficulty == "1.7"):
            difficulty = 1.7
        elif(user_difficulty == "2"):
            difficulty = 2
        else:
            print("Wrong Input: " + user_difficulty)
        save()
    else:
        print("Wrong Input: " + user_action)
