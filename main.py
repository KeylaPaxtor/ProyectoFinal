from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import PokemonAgua, PokemonFuego, PokemonPlanta, PokemonElectrico
import random


def crear_pokemon(opcion):
    datos = CATALOGO_POKEMON[opcion]

    if datos['tipo'] == 'Fuego':
        return PokemonFuego(datos['nombre'], datos['hp_maximo'], datos['energia_maxima'])
    elif datos['tipo'] == 'Agua':
        return PokemonAgua(datos['nombre'], datos['hp_maximo'], datos['energia_maxima'])
    elif datos['tipo'] == 'Planta':
        return PokemonPlanta(datos['nombre'], datos['hp_maximo'], datos['energia_maxima'])
    else:
        return PokemonElectrico(datos['nombre'], datos['hp_maximo'], datos['energia_maxima'])


print('1. Jugador vs Jugador')
print('2. Jugador vs Computadora')

modo_juego = input('Elige modo: ')

mostrar_catalogo_disponible()

# JUGADOR 1
while True:
    opcion_jugador1 = input('Jugador 1: ')
    if opcion_jugador1 in CATALOGO_POKEMON:
        pokemon_jugador1 = crear_pokemon(opcion_jugador1)
        break
    else:
        print('Opción inválida')

# JUGADOR 2 O COMPUTADORA
if modo_juego == '1':
    while True:
        opcion_jugador2 = input('Jugador 2: ')
        if opcion_jugador2 in CATALOGO_POKEMON:
            pokemon_jugador2 = crear_pokemon(opcion_jugador2)
            break
        else:
            print('Opción inválida')
else:
    opcion_computadora = str(random.randint(1, len(CATALOGO_POKEMON)))
    pokemon_jugador2 = crear_pokemon(opcion_computadora)
    print('Computadora eligió', pokemon_jugador2.nombre)

print('\n', pokemon_jugador1.nombre, 'vs', pokemon_jugador2.nombre)

turno_jugador1 = True

while pokemon_jugador1.hp_actual > 0 and pokemon_jugador2.hp_actual > 0:

    if turno_jugador1:
        pokemon_atacante = pokemon_jugador1
        pokemon_defensor = pokemon_jugador2
    else:
        pokemon_atacante = pokemon_jugador2
        pokemon_defensor = pokemon_jugador1

    print('\nTurno de', pokemon_atacante.nombre)
    print('HP:', pokemon_atacante.hp_actual, '/', pokemon_atacante.hp_maximo)
    print('EP:', pokemon_atacante.energia_actual, '/', pokemon_atacante.energia_maxima)

    if pokemon_atacante.paralizado:
        print('Está paralizado y pierde turno')
        pokemon_atacante.paralizado = False
    else:
        print('1. Atacar')
        print('2. Defender')
        print('3. Descansar')

        if modo_juego == '2' and not turno_jugador1:
            opcion_accion = random.randint(1, 3)
            print('Computadora eligió', opcion_accion)
        else:
            try:
                opcion_accion = int(input('Opción: '))
            except:
                opcion_accion = 0

        if opcion_accion == 1:
            pokemon_atacante.atacar(pokemon_defensor)
        elif opcion_accion == 2:
            pokemon_atacante.defender()
        elif opcion_accion == 3:
            pokemon_atacante.descansar()
        else:
            print('Opción inválida')

    turno_jugador1 = not turno_jugador1


print('\nFIN DEL JUEGO')

if pokemon_jugador1.hp_actual <= 0:
    print('Gana', pokemon_jugador2.nombre)
else:
    print('Gana', pokemon_jugador1.nombre)