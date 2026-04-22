# creación de la clase abstracta
from abc import ABC, abstractmethod

class Pokemon(ABC):
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self._nombre = nombre
        self.__hp_actual = hp_maximo
        self.__hp_maximo = hp_maximo
        self.__energia_actual = energia_maxima
        self.__energia_maxima = energia_maxima
        self.defendiendo = False
        self.paralizado = False 

    @property
    def nombre(self):
        return self._nombre

    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, puntos_hp):
        if puntos_hp < 0:
            self.__hp_actual = 0
        elif puntos_hp > self.__hp_maximo:
            self.__hp_actual = self.__hp_maximo
        else:
            self.__hp_actual = puntos_hp

    @property
    def hp_maximo(self):
        return self.__hp_maximo

    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, puntos_energia):
        if puntos_energia < 0:
            self.__energia_actual = 0
        elif puntos_energia > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
        else:
            self.__energia_actual = puntos_energia

    @property
    def energia_maxima(self):
        return self.__energia_maxima

    @abstractmethod
    def atacar(self, rival):
        pass

    def defender(self):
        if self.energia_actual >= 5:
            self.energia_actual -= 5
            self.defendiendo = True
            print(f'{self.nombre} se ha defendido')
        else:
            print('No tienes suficiente energía para defender.')

    def descansar(self):
        self.energia_actual += 20
        print(f'{self.nombre} recuperó energía.')

