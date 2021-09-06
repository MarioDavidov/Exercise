#op(x) for x in team_A if player_to_remove in team_A]
# for num in team_A:
#     if num == player_to_remove:
#         team_A.remove(player_to_remove)
from os import remove


def func(players):
    team_A = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    team_B = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    if player:
        for i in players.split(" "):
            i = i.split('-')
            team = i[0]
            player_to_remove = i[1]
            if team == "A":
                if player_to_remove in team_A:
                    team_A.remove(player_to_remove)
            else:
                if player_to_remove in team_B:
                    team_B.remove(player_to_remove)
            if len(team_A) < 7 or len(team_B) <7:
                break
    if len(team_A) < 7 or len(team_B) < 7:
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
        print('Game was terminated')
    else:
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")


player = input()
func(player)
