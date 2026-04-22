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


def mostrar_estado(pokemon, es_computadora=False):
    print('---------------------------------------------------')

    if es_computadora:
        print('TURNO DE', pokemon.nombre, '(Computadora)')
    else:
        print('TURNO DE', pokemon.nombre)

    print('[HP:', str(pokemon.hp_actual) + '/' + str(pokemon.hp_maximo) + ']',
          '|',
          '[EP:', str(pokemon.energia_actual) + '/' + str(pokemon.energia_maxima) + ']')


def mostrar_acciones():
    print('\n¿Qué acción deseas realizar?\n')
    print('1. Atacar (Costo: 15 EP)')
    print('2. Defender (Costo: 5 EP)')
    print('3. Descansar (Restaura: 20 EP)')


print('===================================================')
print('   SIMULADOR DE BATALLAS POKÉMON (POO)')
print('===================================================')

print('Seleccione el Modo de Juego:')
print('1. Jugador vs Jugador')
print('2. Jugador vs Computadora')

modo_juego = input('> Opción: ')

mostrar_catalogo_disponible()


# Jugador 1
while True:
    opcion_jugador1 = input('Jugador 1, elija el número de su Pokémon: ')
    if opcion_jugador1 in CATALOGO_POKEMON:
        pokemon_jugador1 = crear_pokemon(opcion_jugador1)
        print('¡Has seleccionado a', pokemon_jugador1.nombre + '!')
        break
    else:
        print('Opción inválida')


# Jugador 2 o Computadora
if modo_juego == '1':
    while True:
        opcion_jugador2 = input('Jugador 2, elija el número de su Pokémon: ')
        if opcion_jugador2 in CATALOGO_POKEMON:
            pokemon_jugador2 = crear_pokemon(opcion_jugador2)
            print('¡Has seleccionado a', pokemon_jugador2.nombre + '!')
            es_computadora = False
            break
        else:
            print('Opción inválida')
else:
    print('Computadora eligiendo combatiente...')
    opcion_cpu = str(random.randint(1, len(CATALOGO_POKEMON)))
    pokemon_jugador2 = crear_pokemon(opcion_cpu)
    print('¡La computadora ha seleccionado a', pokemon_jugador2.nombre + '!')
    es_computadora = True


print('\n¡COMIENZA LA BATALLA!')
print(pokemon_jugador1.nombre, 'vs', pokemon_jugador2.nombre)

turno_jugador1 = True


while pokemon_jugador1.hp_actual > 0 and pokemon_jugador2.hp_actual > 0:

    if turno_jugador1:
        atacante = pokemon_jugador1
        defensor = pokemon_jugador2
        turno_computadora = False
    else:
        atacante = pokemon_jugador2
        defensor = pokemon_jugador1
        turno_computadora = es_computadora

    mostrar_estado(atacante, turno_computadora)

    if atacante.paralizado:
        print('Está paralizado y pierde el turno')
        atacante.paralizado = False
    else:
        mostrar_acciones()

        if turno_computadora:  # ✔️ CORREGIDO
            opcion = random.randint(1, 3)
            print('> La computadora elige:', opcion)
        else:
            try:
                opcion = int(input('> Opción: '))
            except:
                opcion = 0

        if opcion == 1:
            atacante.atacar(defensor)
        elif opcion == 2:
            atacante.defender()
        elif opcion == 3:
            atacante.descansar()
        else:
            print('Opción inválida')

        if pokemon_jugador1.hp_actual == 0 or pokemon_jugador2.hp_actual == 0:
            break

    turno_jugador1 = not turno_jugador1


print('---------------------------------------------------')

if pokemon_jugador1.hp_actual <= 0:
    print('¡Gana', pokemon_jugador2.nombre + '!')
else:
    print('¡Gana', pokemon_jugador1.nombre + '!')