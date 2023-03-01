import csv


class pokemon:

    def __init__(self, newpokemon: dict):

        newpokemon['health'] = int(newpokemon['health'])
        newpokemon['defance'] = int(newpokemon['defance'])

        assert newpokemon['health'] >= 0, f"health {newpokemon['health'] } is not greater than or equal to zero!"
        assert newpokemon['defance'] >= 0, f"health {newpokemon['defance']} is not greater than or equal to zero!"

        actions = {}
        for i in range(4):
            actions[newpokemon.get('action'+str(i+1))
                    ] = int(newpokemon.get('attack'+str(i+1)))

        self.name = newpokemon['name']
        self.attack = actions
        self.health = newpokemon['health']
        self.defance = newpokemon['defance']
        self.type = newpokemon['type']

    def __str__(self) -> str:
        return f' pokeman {self.name} with health {self.health} and defence {self.defance} could do this actions : {list(self.attack.keys())}'

    def is_pokemon_dead(self):

        if self.health == 0:
            return True
        else:
            return False

    def update_health(self, damage):
        if damage >= self.defance:
            health = self.health - damage + self.defance
        else:
            health = self.health
        self.set_health(health)

    def set_health(self, h):
        if h < 0:
            self.health = 0
        elif h > 100:
            self.health = 100
        else:
            self.health = h

    @classmethod
    def show_pokemons_list(cls, list_of_existing_pokemons):
        for index, item in enumerate(list_of_existing_pokemons):
            actions = {}
            for i in range(4):
                actions[item.get('action'+str(i+1))
                        ] = int(item.get('attack'+str(i+1)))
            print(
                f" {index} :pokeman {item['name']} with health {item['health']} and defence {item['defance']} could do this actions : {list(actions)}")


def ExtractPokemonsFromCsv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        items = list(reader)
    return items
