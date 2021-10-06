import unittest
from OOP.Guild_system.Player import Player
from OOP.Guild_system.Guild import Guild


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player('Mario', 50, 25)

    def test_setting_attr(self):
        player = Player('Mario', 50, 25)
        self.assertEqual(player.name, 'Mario')
        self.assertEqual(player.hp, 50)
        self.assertEqual(player.mp, 25)
        self.assertEqual(player.guild, 'Unffiliated')
        self.assertEqual(player.skills, {'multicast' : 100})

    def test_add_Skill_method(self):
        result = self.player.add_skill('multicast', 100)
        expected_result = f"Skill multicast added to the collection of the player Mario"
        self.assertEqual(result, expected_result)

    def test_add_skill_when_its_already_in_collection(self):
        result = self.player.add_skill('multicast', 100)
        expected_result = f"Skill already added."
        self.assertEqual(result, expected_result)

    def test_player_info_method(self):
        result = self.player.player_info()
        expected_result = f'Name: Mario\n' \
                          f'Guild: Unffiliated\n' \
                          f'HP: 50\n' \
                          f'MP: 25\n' \
                          f'== multicast - 100\n'
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()


''''
The Player class should receive a name (string), hp (int) and mp (int) upon initialization. The Player also has 2 instance attributes: skills (empty dictionary by initialization – will contain the skills of each player and its mana cost) and guild set to "Unaffiliated" by default.
The Player class should also have two methods:
-	add_skill(skill_name, mana_cost)
o	Add the skill and the corresponding mana cost to the dictionary of skills. Return "Skill {skill_name} added to the collection of the player {player_name}"
o	If the skill is already in the collection, return "Skill already added"

-	player_info() 
o	Returns the player's information, including his/her skills, in this format:
"Name: {player_name}
 Guild: {guild_name}
 HP: {hp}
 MP: {mp}
 ==={skill_name_1} - {skill_mana_cost}
 ==={skill_name_2} - {skill_mana_cost}
 ...
 ==={skill_name_N} - {skill_mana_cost}"

The Guild class receive a name {string}. The Player should also have one instance attribute players (empty list by initialization which will contain the players of the guild). The class also has 3 methods:
-	assign_player(player: Player)
o	Add the player to the guild. Return "Welcome player {player_name} to the guild {guild_name}". Remember to change the player's guild in the player class.
o	If the player is already in the guild, return "Player {player_name} is already in the guild."
o	If the player is in another guild, return "Player {player_name} is in another guild."

-	kick_player(player_name: String)
o	Remove the player from the guild. Return "Player {player_name} has been removed from the guild.". Remember to change the player's guild in the player class to "Unaffiliated".
o	If the is not a player with that name in the guild, return "Player {player_name} is not in the guild."

-	guild_info() 
o	Returns the guild's information, including the players in the guild, in this format:
"Guild: {guild_name}
 {player's info}"

'''
# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.kick_player('salam4e'))
# print(guild.guild_info())
