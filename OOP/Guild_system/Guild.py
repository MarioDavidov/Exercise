from OOP.Guild_system.Player import Player


class Guild:
    players = []

    def __init__(self, name):
        self.name = name

    def assign_player(self, player):
        if player.guild != 'Unffiliated':
            return f'Player {player.name} is in another guild.'
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        self.players.append(player)
        Player.guild = self.name
        return f"Welcome player {player.name} to the guild"

    def kick_player(self, player_name):
        player_to_kick = [x for x in self.players if x.name == player_name]

        if player_to_kick:
            self.players.remove(player_to_kick[0])
            player_to_kick[0].guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        guild_info = f'Guild: {self.name}\n'
        for player in self.players:
            guild_info += player.player_info()

        return guild_info