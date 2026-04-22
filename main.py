from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import PokemonAgua, PokemonFuego, PokemonPlanta, PokemonElectrico
import random


# ======================
# CREAR POKÉMON
# ======================
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


# ======================
# FUNCIONES DE VISUALIZACIÓN
# ======================
def mostrar_menu_principal():
    print('===================================')
    print(' SIMULADOR DE BATALLAS POKÉMON')
    print('===================================')
    print('1. Jugador vs Jugador')
    print('2. Jugador vs Computadora')


def mostrar_estado(pokemon, es_computadora=False):
    print('\n-----------------------------------')
    if es_computadora:
        print('Turno de la Computadora (', pokemon.nombre, ')')
    else:
        print('Turno de', pokemon.nombre)

    print('HP:', pokemon.hp_actual, '/', pokemon.hp_maximo)
    print('EP:', pokemon.energia_actual, '/', pokemon.energia_maxima)


def mostrar_acciones():
    print('1. Atacar')
    print('2. Defender')
    print('3. Descansar')


def mostrar_ganador(jugador1, jugador2):
    print('\nFIN DEL JUEGO')
    if jugador1.hp_actual <= 0:
        print('Gana', jugador2.nombre)
    else:
        print('Gana', jugador1.nombre)


# ======================
# FUNCIONES DE ENTRADA
# ======================
def pedir_modo_juego():
    while True:
        modo = input('Elige modo: ')
        if modo in ['1', '2']:
            return modo
        else:
            print('Opción inválida')


def pedir_pokemon(mensaje):
    while True:
        opcion = input(mensaje)
        if opcion in CATALOGO_POKEMON:
            return opcion
        else:
            print('Opción inválida')


def pedir_accion():
    try:
        return int(input('Opción: '))
    except:
        return 0


# ======================
# PROGRAMA PRINCIPAL
# ======================

mostrar_menu_principal()
modo_juego = pedir_modo_juego()

mostrar_catalogo_disponible()

# Jugador 1
opcion_jugador1 = pedir_pokemon('Jugador 1: ')
pokemon_jugador1 = crear_pokemon(opcion_jugador1)

# Jugador 2 o Computadora
if modo_juego == '1':
    opcion_jugador2 = pedir_pokemon('Jugador 2: ')
    pokemon_jugador2 = crear_pokemon(opcion_jugador2)
    es_computadora = False
else:
    opcion_computadora = str(random.randint(1, len(CATALOGO_POKEMON)))
    pokemon_jugador2 = crear_pokemon(opcion_computadora)
    print('La Computadora eligió', pokemon_jugador2.nombre)
    es_computadora = True


print('\n', pokemon_jugador1.nombre, 'vs', pokemon_jugador2.nombre)

turno_jugador1 = True

while pokemon_jugador1.hp_actual > 0 and pokemon_jugador2.hp_actual > 0:

    if turno_jugador1:
        atacante = pokemon_jugador1
        defensor = pokemon_jugador2
        turno_es_computadora = False
    else:
        atacante = pokemon_jugador2
        defensor = pokemon_jugador1
        turno_es_computadora = es_computadora

    mostrar_estado(atacante, turno_es_computadora)

    if atacante.paralizado:
        print('Está paralizado y pierde turno')
        atacante.paralizado = False
    else:
        mostrar_acciones()

        if turno_es_computadora:
            opcion = random.randint(1, 3)
            print('La Computadora eligió', opcion)
        else:
            opcion = pedir_accion()

        if opcion == 1:
            atacante.atacar(defensor)
        elif opcion == 2:
            atacante.defender()
        elif opcion == 3:
            atacante.descansar()
        else:
            print('Opción inválida')

    turno_jugador1 = not turno_jugador1


mostrar_ganador(pokemon_jugador1, pokemon_jugador2)