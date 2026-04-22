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