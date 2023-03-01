from abc import ABC, abstractclassmethod
from pokemon import *
import random
import sys


class player(ABC):

    def __init__(self, name, list_of_existing_pokemons) -> None:
        super().__init__()
        self.list_of_existing_pokemons = list_of_existing_pokemons
        self.name = name
        self.pokemon_list = []
        self.current_pokemon = None

    @abstractclassmethod
    def player_turn():
        pass

    def update_health(self, damage):
        self.current_pokemon.update_health(damage)

    def is_player_dead(self):
        death = True
        for items in self.pokemon_list:
            if not items.is_pokemon_dead():
                death = False
        return death

    def show_pokemons_status(self):
        print(f"\n**************** {self.name}'s pokemons **************\n")
        for i, x in enumerate(self.pokemon_list):
            print(f"{i+1}.", x)

    def show_player_move(self, move):
        print(f"\n************** {self.name} attack *********************\n")
        print(
            f"{self.name} go with pokemon {self.current_pokemon.name} and action {move} for this round")


class real_player(player):

    def __init__(self, name, list_of_existing_pokemons) -> None:
        super().__init__(name, list_of_existing_pokemons)

    def initialize_input_pokemons(self):
        if len(self.pokemon_list) < 4:
            print('\n************initializing pokemons*************************\n')
            print(f"you can choose 4 pokemons. please select your pokemons form the list below(order is important):\n")
            for i in range(4 - len(self.pokemon_list)):
                pokemon.show_pokemons_list(self.list_of_existing_pokemons)
                while (True):
                    try:
                        choice = self.list_of_existing_pokemons[int(
                            input('\nenter the pokemon number:  '))]
                        break
                    except KeyboardInterrupt:
                        sys.exit()
                    except:
                        print('your input number is not correct please try again')

                pokemon_name = pokemon(choice)
                self.pokemon_list.append(pokemon_name)

        else:
            print('\n************you already choose your 4 pokemons*****************\n')

        self.current_pokemon = self.pokemon_list[0]

    def select_pokemon(self):
        print('\n************selecting main pokemon*************************\n')
        # try:
        #     act = int(input(
        #         'press one to countinue with attack sequence or two for choose another pokemon  '))

        # except KeyboardInterrupt:
        #     sys.exit()
        # except:
        #     print('your input number is not correct please try again')

        # if act == 1:
        #     pockemonindex = self.pokemon_list.index(self.current_pokemon)
        #     self.current_pokemon = self.pokemon_list[pockemonindex+1]

        # if act == 2:
        print('please select one pokemon as your pokemon for this round')
        while (True):
            try:
                self.current_pokemon = self.pokemon_list[int(
                    input('enter the pokemon number:  '))-1]
                if self.current_pokemon.is_pokemon_dead():
                    print('your selected pokemon is fainted please try again')
                    continue
                else:
                    break
            except KeyboardInterrupt:
                sys.exit()
            except:
                print('your input number is not correct please try again')

    def select_next_move(self):
        print("\n************selecting pokemon's move*************************\n")
        print('your selected pokemon can do')
        attacks = self.current_pokemon.attack
        i = 1
        for key, val in attacks.items():
            print(f'{i}.move {key} with a attack {val}')
            i += 1
        while (True):
            try:
                move = list(attacks.keys())[
                    int(input("enter move's number:  "))-1]
                break
            except KeyboardInterrupt:
                sys.exit()
            except:
                print('your input number is not correct please try again')

        attack_power = attacks[move]
        return attack_power, move

    def player_turn(self):

        self.initialize_input_pokemons()
        self.show_pokemons_status()
        self.select_pokemon()
        attack_power, move = self.select_next_move()
        self.show_player_move(move)
        return self.current_pokemon.type, attack_power


class computer_player(player):
    def initialize_input_pokemons(self):
        if len(self.pokemon_list) < 4:
            choices = random.sample(self.list_of_existing_pokemons, 4)
            for item in choices:
                pokemon_name = pokemon(item)
                self.pokemon_list.append(pokemon_name)

    def select_pokemon(self):
        mainpokemon = random.sample(self.pokemon_list, 1)[0]
        while (mainpokemon.is_pokemon_dead()):
            mainpokemon = random.sample(self.pokemon_list, 1)[0]
        self.current_pokemon = mainpokemon

    def select_next_move(self):
        attacks = self.current_pokemon.attack
        move = random.sample(attacks.keys(), 1)[0]
        attack_power = attacks[move]
        return attack_power, move

    def player_turn(self):

        self.initialize_input_pokemons()
        self.show_pokemons_status()
        self.select_pokemon()
        attack_power, move = self.select_next_move()
        self.show_player_move(move)
        return self.current_pokemon.type, attack_power
