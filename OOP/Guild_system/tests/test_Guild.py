import unittest
from OOP.Guild_system.Guild import Guild
from OOP.Guild_system.Player import Player


class TestGuild(unittest.TestCase):
    def test_setting_attr(self):
        guild = Guild('theguild')
        self.assertEqual(guild.name, 'theguild')

    def test_assign_player(self):
        player = Player('Mario', 50,50)
        guild_assign_player = Guild('assign')

        result1 = guild_assign_player.assign_player(player)
        expected_result2 = 'Welcome player Mario to the guild'
        self.assertEqual(result1, expected_result2)

    def test_assign_to_the_same_guild(self):
        player = Player('Mario', 50, 50)
        guild_assign_player = Guild('assign')

        result1 = guild_assign_player.assign_player(player)
        expected_result2 = 'Player Mario is in another guild.'
        self.assertEqual(result1, expected_result2)

    def test_assign_player_with_guild_to_other_guild(self):
        player = Player('Mario', 50, 50)
        guild_assign_player = Guild('assign')
        guild_assign_player.assign_player(player)
        second_guild = Guild('assign_with_guild')
        result1 =  second_guild.assign_player(player)
        expected_result2 = 'Player Mario is in another guild.'
        self.assertEqual(result1, expected_result2)


    def test_kick_player(self):
        player = Player('Mario', 50, 50)
        guild_assign_player = Guild('assign')
        guild_assign_player.assign_player(player)

        result = guild_assign_player.kick_player('Mario')
        expected_result = 'Player Mario has been removed from the guild.'
        self.assertEqual(result, expected_result)

        result2 = guild_assign_player.kick_player('Mario')
        expected_result2 = "Player Mario is not in the guild."
        self.assertEqual(result2, expected_result2)

    def test_get_info_about_guild(self):
        player = Player('Mario', 50, 50)
        player.add_skill('firecast', 500)
        guild_assign_player = Guild('assign')
        guild_assign_player.assign_player(player)

        result = guild_assign_player.guild_info()
        expected_result =   f'Guild: assign\n' \
                            f'Name: Mario\n' \
                            f'Guild: assign\n' \
                            f'HP: 50\n' \
                            f'MP: 50\n' \
                            f'== firecast - 500\n'
        self.assertEqual(result, expected_result)