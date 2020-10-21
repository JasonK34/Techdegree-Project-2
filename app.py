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

def balance_teams():
    
    global players_list
    global players_copy
    global panthers_players
    global bandits_players
    global warriors_players

    panthers_players = random.sample(players_list, 6)
    players_list = [x for x in players_list if x not in panthers_players]
    
    bandits_players = random.sample(players_list, 6)
    players_list = [x for x in players_list if x not in bandits_players]

    warriors_players = random.sample(players_list, 6)
    players_list = [x for x in players_list if x not in warriors_players]

    
def stat_tool():
    try:
        initial_entry = int(input("\nPlease enter '1' for STATS, and '2' to QUIT: \n\n ---> "))
        while initial_entry == 1:
            select_team = int(input("\nSelect option below (enter number):\n\n (1) PANTHERS roster\n (2) BANDITS roster\n (3) WARRIORS roster \n (4) All Guardians\n (5) QUIT PROGRAM\n\n ---> "))
            if select_team == 1:
                print("\nPANTHERS: \n")
                print("Number of players: ", len(panthers_players))
                print(*panthers_players, sep=", ")
 
            if select_team == 2:
                print("\nBANDITS: \n")
                print("Number of players: ", len(bandits_players))
                print(*bandits_players, sep=", ")
            
            if select_team == 3:
                print("\nWARRIORS: \n")
                print("Number of players: ", len(warriors_players))            
                print(*warriors_players, sep=", ")  
                                       
            if select_team == 4:
                print("\nGUARDIANS: \n")
                for guardian in guardian_list:
                    print(guardian)
            if select_team == 5:
                print("\nGoodbye\n")
                break
        if initial_entry == 2:
            print("\nGoodbye!\n")
        if initial_entry != 1 and initial_entry != 2:
            print("Invalid entry")
            stat_tool()
            
    except ValueError:
        print("Invalid Entry")
        stat_tool()

        

        

if __name__ == "__main__":
    clean_data()
    balance_teams()
    stat_tool()

    

