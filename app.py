#TechDegree Project 2 - Basketball Stats tool

from constants import TEAMS
from constants import PLAYERS
import copy
import random


players_copy = copy.deepcopy(PLAYERS)
teams_copy = copy.deepcopy(TEAMS)

players_list = []
guardian_list = []

panthers_players = []
bandits_players = []
warriors_players = []

print("\nWelcome to Basketball Stats!\n")

def clean_data():
    
    for player in players_copy:
        for key, value in player.items():
            if key == "name":
                players_list.append(value)

            if key == "guardians":
                guardians = value.split('and')
                player["guardians"] = guardians
                for guardian in guardians:
                    guardian_list.append(guardian)

            if key == "height":
                height = int(value.split(" ")[0])
                player["height"] = height
                
            if key == "experience":
                if "experience" == "YES":
                    player["experience"] = True
                if "experience" == "NO":
                    player["experience"] = False

def balance_teams(players_copy):
    
    print (players_copy)
    panthers_players = random.sample(players_copy, 6)
    print('\n', panthers_players)
    players_copy = [x for x in players_copy if x not in panthers_players]
    
    bandits_players = random.sample(players_copy, 6)
    print('\n', bandits_players)
    players_copy = [x for x in players_copy if x not in bandits_players]

    warriors_players = random.sample(players_copy, 6)
    print('\n', warriors_players)
    players_copy = [x for x in players_copy if x not in warriors_players]

    # each team is assigned 6 players and they show up when printed here, but when the stat_tool runs these lists are empty
    
def stat_tool():

    initial_entry = int(input("\nPlease enter '1' for stats, and '2' to exit: \n\n ---> "))
    while initial_entry == 1:
        select_team = int(input("\nSelect option below (enter numer):\n (1) PANTHERS roster\n (2) BANDITS roster\n (3) WARRIORS roster \n (4) ALL Players\n (5) All Guardians\n\n ---> "))
        if select_team == 1:
            print("\nPANTHERS: \n")
            print(panthers_players)  #this is just here to see if it prints the list, but it is empty and I cannot figure out why; it happens with all 3 teams
            for panther in panthers_players:             
                for key, value in panther.items():
                    if key == "name":
                        print(value)
                    if key == "height":
                        print(" * Height: ", value, "inches")
                    if key == "guardians":
                        print(" * Guardian(s): ", ','.join(value))
                    if key == "experience":
                        print(" * Experience: ", value)

        if select_team == 2:
            print("\nBANDITS: \n")
            print(bandits_players)
            for bandit in bandits_players:
                for key, value in bandit.items():
                    if key == "name":
                        print(value)
                    if key == "height":
                        print(" * Height: ", value, "inches")
                    if key == "guardians":
                        print(" * Guardian(s): ", ','.join(value))
                    if key == "experience":
                        print(" * Experience: ", value)    
        if select_team == 3:
            print("\nWARRIORS: \n")
            print(warriors_players)
            for warrior in warriors_players:
                for key, value in warrior.items():
                    if key == "name":
                        print(value)
                    if key == "height":
                        print(" * Height: ", value, "inches") 
                    if key == "guardians":
                        print(" * Guardian(s): ", ','.join(value))
                    if key == "experience":
                        print(" * Experience: ", value)   
                        
        if select_team == 4:
            print("ALL players: \n")
            for player in players_list:
                print(player)
                
        if select_team == 5:
            print("\nGUARDIANS: \n")
            for guardian in guardian_list:
                print(guardian)    
                                 
                                    
if __name__ == "__main__":
    clean_data()
    balance_teams(players_copy)
    stat_tool()

    


