import random

player_list = [] # names
pet_list = []

player_dict = {} # 'playername': level
pet_dict = {} # 'petname': level

finished = ''
i = 0

while len(finished) == 0:
    player_list.append(input("Player name:"))
    player_dict[player_list[-1]] = int(input("Player level:"))
    pet_list.append(input("Pet name:"))
    pet_dict[pet_list[-1]] = int(input("Pet level:"))
    finished = input('Press enter to add another player-pet pair...')

print(len(player_list), "player-pet pairs registered.")

pair_avgs = {}
for i in range(len(player_dict),0,-1):
    print("Average level of pair", player_list[i-1], "+", pet_list[i-1],":")
    pair_avgs[player_list[i-1]+":"+ pet_list[i-1]] = (player_dict[player_list[i-1]]+pet_dict[pet_list[i-1]])/2
    print(pair_avgs[player_list[i-1]+":"+ pet_list[i-1]])

teamsize = int(input("Choose team size:"))

pair_names = pair_avgs.keys()

avg_threshold = int(input("Enter treshold for team combo:"))
itermax = 100
iter = 0
teamavg = 0

while (iter <= itermax) and (teamavg <= avg_threshold):
    iter += 1

    teamavg = 0
    team = random.sample(pair_names, teamsize)
    print(team)
    for pair in team:
        teamavg += pair_avgs[pair]
    teamavg = teamavg / teamsize
    print("Team average:", round(teamavg))

with open('testlvls.txt') as f:
    line_info = []
    for line in f:
        word = ''
        for c in line:
            if (c != ' ') and (c != '\n'):
                word += c
            else:
                try:
                    word = int(word)
                    line_info.append(word)
                    word = ''
                except:
                    line_info.append(word)
                    word = ''

