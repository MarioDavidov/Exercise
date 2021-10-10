import unittest
from OOP.Guild_system.Player import Player

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
