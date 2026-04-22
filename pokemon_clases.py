from pokemon import Pokemon
import random


class PokemonAgua(Pokemon):
    def atacar(self, rival):
        if self.energia_actual < 15:
            print('No tienes energía suficiente para poder atacar')
            return

        daño = 10

        if isinstance(rival, PokemonFuego):
            daño *= 2
            print('¡Es súper efectivo!')
        elif isinstance(rival, PokemonPlanta):
            print('No es muy efectivo...')

        if rival.defendiendo:
            daño //= 2
            rival.defendiendo = False

        self.energia_actual -= 15
        rival.hp_actual -= daño
        print(f'{self.nombre} hace {daño} de daño')


class PokemonFuego(Pokemon):
    def atacar(self, rival):
        if self.energia_actual < 15:
            print('No tienes energía suficiente para poder atacar.')
            return

        daño = 10

        if isinstance(rival, PokemonPlanta):
            daño *= 2
            print('¡Es súper efectivo!')
        elif isinstance(rival, PokemonAgua):
            print('No es muy efectivo...')

        if rival.defendiendo:
            daño //= 2
            rival.defendiendo = False

        self.energia_actual -= 15
        rival.hp_actual -= daño
        print(f'{self.nombre} hace {daño} de daño')


class PokemonPlanta(Pokemon):
    def atacar(self, rival):
        if self.energia_actual < 15:
            print('No tienes energía suficiente para poder atacar.')
            return

        daño = 10

        if isinstance(rival, PokemonAgua):
            daño *= 2
            print('¡Es súper efectivo!')
        elif isinstance(rival, PokemonFuego):
            print('No es muy efectivo...')

        if rival.defendiendo:
            daño //= 2
            rival.defendiendo = False

        self.energia_actual -= 15
        rival.hp_actual -= daño
        print(f'{self.nombre} hace {daño} de daño')


class PokemonElectrico(Pokemon):
    def atacar(self, rival):
        if self.energia_actual < 15:
            print('No tienes energía suficiente para poder atacar.')
            return

        daño = 10

        if rival.defendiendo:
            daño //= 2
            rival.defendiendo = False

        if random.random() < 0.2:
            rival.paralizado = True
            print('El rival ha sido paralizado!')

        self.energia_actual -= 15
        rival.hp_actual -= daño
        print(f'{self.nombre} hace {daño} de daño')