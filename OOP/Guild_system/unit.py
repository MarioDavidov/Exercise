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

# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.kick_player('salam4e'))
# print(guild.guild_info())
