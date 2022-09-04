import sys
import time
import random

import extras.save
import extras.skills
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
playing = True

# Enemies and their vars
enemy_t1 = extras.enemies.tier1
enemy_t2 = extras.enemies.tier2
enemy_t3 = extras.enemies.tier3
enemy_t4 = extras.enemies.tier4
enemy_t5 = extras.enemies.tier5

# Functions
def Fight(enemy,ph,pmh,ps,pd,pg,pa,pw,px):
    e_health = enemy.e_health
    e_strength = enemy.e_strength
    e_defense = enemy.e_defense
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
        pg = pg + (100 * e_tier)
        print("You have been healed!")
        ph = pmh
        px = px + e_tier * 100
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
    global end_pg
    end_pg = pg
    global end_w
    end_w = pw
    global end_a
    end_a = pa
    global end_s
    end_s = ps
    global end_d
    end_d = pd
    global end_h
    end_h = ph
    global end_x
    end_x = px


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

    global end_a_2
    end_a_2 = a
    global end_w_2
    end_w_2 = w
    global end_s_2
    end_s_2 = ps
    global end_d_2
    end_d_2 = pd
    global end_sp
    end_sp = psp








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

    user_action = input("What do you want to do? (exit,fight,stats,shop,skills,about) ---> ")
    # Exit and save
    if(user_action == "exit"):
        playing = False
        file_open = open(file="extras\\save.py",mode="w")
        skillz_open = open(file="extras\\skills.py",mode="w")
        file_open.write("health = " + str(health) + "\n" + "max_health = " + str(max_health) + "\n" + "strength = " + str(strength) + "\n" + "defense = " + str(defense) + "\n" + "gold = " + str(gold) + "\n" + "armour = " + str(str(armour)) + " " + "\n" + "weapon = " + str(str(weapon)) + " " + "\n" + "xp = " + str(xp) + " " + "\n" + "skillpoints = " + str(skillpoints) + " " + "\n")
        skillz_open.write("a = " + str(a) + " " + "\n" + "w = " + str(w) + " " + "\n")
        sys.exit()
    elif(user_action == "stats"):
        print("health = " + str(health) + "\n" + "max_health = " + str(max_health) + "\n" + "strength = " + str(strength) + "\n" + "defense = " + str(defense) + "\n" + "gold = " + str(gold) + "g\n" + "armour = " + str(armour) + " " + "\n" + "weapon = " + str(weapon) + " " + "\n" + "xp = " + str(xp) + " " + "\n" + "skillpoints = " + str(skillpoints) + " " + "\n")
        print("a = " + str(a) + " " + "\n" + "w = " + str(w) + " " + "\n")
    elif(user_action == "fight"):
        user_wanted_fight = input("What tier do you want to fight? (1,2,3,4,5) ---> ")
        if(user_wanted_fight == "1"):
            Fight(enemy=enemy_t1,ph=health,pmh=max_health,ps=strength,pd=defense,pg=gold,pa=armour,pw=weapon,px=xp)
            gold = end_pg
            weapon = end_w
            armour = end_a
            strength = end_s
            defense = end_d
            health = end_h
            xp = end_x
        elif(user_wanted_fight == "2"):
            Fight(enemy=enemy_t2,ph=health,pmh=max_health,ps=strength,pd=defense,pg=gold,pa=armour,pw=weapon,px=xp)
            gold = end_pg
            weapon = end_w
            armour = end_a
            strength = end_s
            defense = end_d
            health = end_h
            xp = end_x
        elif(user_wanted_fight == "3"):
            Fight(enemy=enemy_t3,ph=health,pmh=max_health,ps=strength,pd=defense,pg=gold,pa=armour,pw=weapon,px=xp)
            gold = end_pg
            weapon = end_w
            armour = end_a
            strength = end_s
            defense = end_d
            health = end_h
            xp = end_x
        elif (user_wanted_fight == "4"):
            Fight(enemy=enemy_t4, ph=health, pmh=max_health, ps=strength, pd=defense, pg=gold, pa=armour, pw=weapon,px=xp)
            gold = end_pg
            weapon = end_w
            armour = end_a
            strength = end_s
            defense = end_d
            health = end_h
            xp = end_x
        elif (user_wanted_fight == "5"):
            Fight(enemy=enemy_t5, ph=health, pmh=max_health, ps=strength, pd=defense, pg=gold, pa=armour, pw=weapon,px=xp)
            gold = end_pg
            weapon = end_w
            armour = end_a
            strength = end_s
            defense = end_d
            health = end_h
            xp = end_x



    elif(user_action == "shop"):
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
            if(gold >= 1000):
                gold = gold - 1000
                strength = strength + 1
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 1000 required!")
        elif(user_wanted_buy == "B"):
            if(gold >= 1000):
                gold = gold - 1000
                defense = defense + 1
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 1000 required!")
        elif(user_wanted_buy == "C"):
            if(gold >= 100):
                gold = gold - 100
                strength = strength - weapon
                weapon = 1
                strength = strength + weapon
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 100 required!")
        elif(user_wanted_buy == "D"):
            if(gold >= 2000):
                gold = gold - 2000
                strength = strength - weapon
                weapon = 5
                strength = strength + weapon
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 2000 required!")
        elif(user_wanted_buy == "E"):
            if(gold >= 100):
                gold = gold - 100
                defense = defense - armour
                armour = 1
                defense = defense + armour
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 100 required!")
        elif(user_wanted_buy == "F"):
            if(gold >= 2000):
                gold = gold - 2000
                defense = defense - armour
                armour = 5
                defense = defense + armour
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 2000 required!")
        elif(user_wanted_buy == "G"):
            if(gold >= 5000):
                gold = gold - 5000
                strength = strength - weapon
                weapon = 10
                strength = strength + weapon
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 5000 required!")
        elif(user_wanted_buy == "H"):
            if(gold >= 10000):
                gold = gold - 10000
                strength = strength - weapon
                weapon = 20
                strength = strength + weapon
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 10000 required!")
        elif(user_wanted_buy == "I"):
            if(gold >= 5000):
                gold = gold - 5000
                defense = defense - armour
                armour = 10
                defense = defense + armour
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 5000 required!")
        elif(user_wanted_buy == "J"):
            if(gold >= 10000):
                gold = gold - 10000
                defense = defense - armour
                armour = 20
                defense = defense + armour
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 10000 required!")
        elif(user_wanted_buy == "K"):
            if(gold >= 20000):
                gold = gold - 20000
                strength = strength - weapon
                weapon = 50
                strength = strength + weapon
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 20000 required!")
        elif(user_wanted_buy == "L"):
            if (gold >= 50000):
                gold = gold - 50000
                strength = strength - weapon
                weapon = 100
                strength = strength + weapon
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 50000 required!")
        elif(user_wanted_buy == "M"):
            if (gold >= 20000):
                gold = gold - 20000
                defense = defense - armour
                armour = 50
                defense = defense + armour
                print("Purchase successful!")
            else:
                print("You dont have enough gold! 20000 required!")
        elif(user_wanted_buy == "N"):
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

    elif(user_action == "skills"):
        SkillAdd(psp=skillpoints,a=a,w=w,ps=strength,pd=defense)
        strength = end_s_2
        defense = end_d_2
        skillpoints = end_sp
        a = end_a_2
        w = end_w_2

    elif(user_action == "about"):
        print("Game was made by me!")
        print("Follow my yt if you want!")
        print("https://www.youtube.com/channel/UCME-adZK2Rqb4mToqqSqApQ")
        print("Version: 1.0")

    else:
        print("Wrong Input: " + user_action)
