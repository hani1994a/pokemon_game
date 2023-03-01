from game_manager import *
from pokemon import *
from player import real_player, computer_player

# TODO: read path from setting
game_logic = ExtractPokemonLogicMatrix(r".\chart.csv")

list_of_existing_pokemons = ExtractPokemonsFromCsv(
    r".\pokemon.csv")

# TODO: get the user name from the input
player1 = real_player(
    name='hani', list_of_existing_pokemons=list_of_existing_pokemons)
player2 = computer_player(
    name='computer', list_of_existing_pokemons=list_of_existing_pokemons)
# we can play with 2 humans by uncommenting the following.
# player2 = computer_player(
#     name='player2', list_of_existing_pokemons=list_of_existing_pokemons)
game1 = game_manager(player1, player2, game_logic)
game1.start()
