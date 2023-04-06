import random

# READING LEVELS TXT
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
    line_info.append(int(word))

# CREATING PLAYER AND PET INFO
player_list = [str(int(i/4))+line_info[i] for i in range(0,len(line_info),4)]  # names
pet_list = [str(int(i/4))+line_info[i] for i in range(2,len(line_info),4)]

player_dict = {}  # 'playername': level
pet_dict = {}  # 'petname': level

for i in range(0, int(len(line_info) / 4)):
    player_dict[player_list[i]] = line_info[1 + i * 4]
    pet_dict[pet_list[i]] = line_info[3 + i * 4]

i = 0

'''
while len(finished) == 0:
    player_list.append(input("Player name:"))
    player_dict[player_list[-1]] = int(input("Player level:"))
    pet_list.append(input("Pet name:"))
    pet_dict[pet_list[-1]] = int(input("Pet level:"))
    finished = input('Press enter to add another player-pet pair...')
'''

print(len(player_list), "player-pet pairs registered.")

pair_avgs = {}
for i in range(0,len(player_dict)):
    print("Average level of pair", player_list[i-1][1:], "+", pet_list[i-1][1:],":")
    pair_avgs[player_list[i-1][1:]+":"+ pet_list[i-1][1:]] = (player_dict[player_list[i-1]]+pet_dict[pet_list[i-1]])/2
    print(pair_avgs[player_list[i-1][1:]+":"+ pet_list[i-1][1:]])

teamsize = int(input("Choose team size:"))

pair_names = pair_avgs.keys()

avg_threshold = int(input("Enter treshold for team combo:"))
itermax = 100
iter = 0
teamavg = 0
combo_teams = []

while (iter <= itermax):
    iter += 1

    teamavg = 0
    team = random.sample(pair_names, teamsize)
    team.sort()
    for pair in team:
        teamavg += pair_avgs[pair]
    teamavg = teamavg / teamsize
    if teamavg >= avg_threshold and team not in combo_teams:
        combo_teams.append(team)
        print("Team average:", round(teamavg))
