from pokemon import Pokemon

class PokemonAgua(Pokemon):
    def atacar(self, rival):
        if self.energia_actual < 15:
            print('No tienes energía suficiente para poder atacar')
            return

        daño = 10

        if rival.tipo == 'Fuego':
            daño *= 2
            print('¡Súper efectivo!')

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

        if rival.tipo == 'Planta':
            daño *= 2
            print('¡Súper efectivo!')

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

        if rival.tipo == 'Agua':
            daño *= 2
            print('Ataque efectivo')

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
            print('El rival ha sido paralizado')

        self.energia_actual -= 15
        rival.hp_actual -= daño
        print(f'{self.nombre} hace {daño} de daño')