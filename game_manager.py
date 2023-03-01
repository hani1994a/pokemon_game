import pandas as pd
from player import player


class game_manager:

    def __init__(self, player1: player, player2: player, matrix) -> None:
        self.player1 = player1
        self.player2 = player2
        self.matrix = matrix
        self.round = 1

    def fight_eeffectivness(self, type1, type2):
        effect_player1onplayer2 = self.matrix.loc[type1, type2]
        effect_player2onplayer1 = self.matrix.loc[type2, type1]
        return effect_player1onplayer2, effect_player2onplayer1

    def starting_round(self):
        print(
            f'\n################################################################  round {self.round} ##########################################################################################\n')
        print(f'{self.player1.name} VS {self.player2.name}')

    def calculate_damage(self, player1_attack, player2_attack, player1_type, player2_type):
        effect_player1onplayer2, effect_player2onplayer1 = self.fight_eeffectivness(
            player1_type, player2_type)
        damage1 = effect_player2onplayer1*player2_attack
        damage2 = effect_player1onplayer2*player1_attack
        return damage1, damage2

    def is_game_finished(self):

        if self.player1.is_player_dead() == True:
            print('The game finished')
            print(f"{self.player1.name}'s pokemons all fainted and loose the game")
            return True
        elif self.player2.is_player_dead() == True:
            print(f"{self.player2.name}'s pokemons all fainted and loose the game")
            return True
        else:
            return False

    def game_status(self, damage1, damage2):
        print("\n************* battel start *************\n")
        if damage1 > damage2:
            print(f"{self.player2.name} attack is effective")
        elif damage1 < damage2:
            print(f"{self.player1.name} attack is effective")
        else:
            print("Attacks are the same.")
        print("battel finished. your pokemons health are updating")

    def start(self):

        while (True):

            self.starting_round()
            player1_type, player1_attack = self.player1.player_turn()
            player2_type, player2_attack = self.player2.player_turn()
            damage_player1, damage_player2 = self.calculate_damage(
                player1_attack, player2_attack, player1_type, player2_type)
            self.game_status(damage_player1, damage_player2)
            self.player1.update_health(damage_player1)
            self.player2.update_health(damage_player2)
            self.round += 1

            if self.is_game_finished() == True:
                break


def ExtractPokemonLogicMatrix(path):
    data = pd.read_csv(path)
    data = data.set_index('Attacking')
    return data
