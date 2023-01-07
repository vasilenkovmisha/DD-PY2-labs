# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


class Car:
    def __init__(self, name: str, max_speed: Union[int, float], price: Union[int, float]):
        """
           Метод - констркутор. Инициализирует объект значениями.
           принимает на вход название, макс.скорость и стоимость автомобиля.

           >>> lada = Car('Лада', 120, 500000)
           >>> lada.car_tax(110)
           50000.0
        """
        if not isinstance(name, str):
            raise TypeError('Название автомобиля должно быть строкой!')
        if not isinstance(max_speed, (int, float)):
            raise TypeError('Скорость может быть только целым или дробным числом!')
        if max_speed < 0:
            raise ValueError('Скорость не может быть отрицательной!')
        if not isinstance(price, (int, float)):
            raise TypeError('Стоимость может быть только целым или дробным числом!')
        if price < 0:
            raise ValueError('Стоимость не может быть отрицательной!')
        self.name = name
        self.max_speed = max_speed
        self.price = price

    def print_info(self):
        """Метод печатает информацию об автомобиле."""
        print(f'Автомобиль - {self.name}, стоимостью - {self.price} руб.\nМакс.скорость: {self.max_speed} км/ч.')

    def car_tax(self, horsepower: Union[int, float]):
        """Метод рассчитывает налог на автомобиль.
           Метод принимает на вход количество лошадиных сил, а возвращает налог в рублях.
           Налог рассчитывается следующим образом: если кол-во лошадиных сил больше 100,
           то налог составляет 10 процентов от стоимости, иначе 5 процентов.
        """
        if not isinstance(horsepower, (int, float)):
            raise TypeError('Кол-во лошадиных сил может быть только целым или дробным числом!')
        if horsepower < 0:
            raise ValueError('Кол-во лошадиных сил не может быть отрицательным!')
        if horsepower > 100:
            return self.price * 0.1
        return self.price * 0.05

class Phone:
    def __init__(self, name: str, smart: bool, os: str, ram: int):
        """
           Метод - констркутор. Инициализирует объект значениями.
           принимает на вход название, тип устойства, операцинную систему и кол-во ОЗУ.
           >>> iphone_xr = Phone('Iphone XR', True, 'IOS', 2)
           >>> iphone_xr.check_ram(3)
           False
        """
        if not isinstance(name, str):
            raise TypeError('Название телефона должно быть строкой!')
        if not isinstance(smart, bool):
            raise TypeError('Телефон либо смартфон, либо нет!')
        if not isinstance(os, str):
            raise TypeError('Тип ОС должен быть строкой!')
        if not isinstance(ram, int):
            raise TypeError('Количество оперативной памяти должно быть целым числом!')
        if ram < 0:
            raise ValueError('Количество оперативной памяти не может быть отрицательным!')
        self.name = name
        self.smart = smart
        self.os = os
        self.ram = ram

    def print_info(self):
        """Метод печатает информацию об телефоне."""
        print(f'Телефон - {self.name} на операционной системе - {self.os}.\nОперативная память: {self.ram} гб.')

    def check_ram(self, count_ram):
        """Метод проверяет, хватит ли телефону оперативной памяти для программы
           Принимает на вход количество требуемой ОЗУ для корректной работы программы
        """
        return self.ram >= count_ram

class Bed:
    def __init__(self, weight: Union[int, float], length: Union[int, float], capacity: int):
        """
           Метод - констркутор. Инициализирует объект значениями.
           принимает на вход ширину, длину и вместительность кровати.
           >>> bed1 = Bed(200, 200, 2)
           >>> bed1.check_room(400, 150)
           False
        """
        if not isinstance(weight, (int, float)):
            raise TypeError('Ширина кровати может быть только целым или дробным числом!')
        if not isinstance(length, (int, float)):
            raise TypeError('Длина кровати может быть только целым или дробным числом!')
        if not isinstance(capacity, int):
            raise TypeError('Вместительность может быть только целым числом!')

        if weight < 0:
            raise ValueError('Ширина не может быть отрицательным числом!')
        if length < 0:
            raise ValueError('Длина не может быть отрицательным числом!')
        if capacity < 1:
            raise ValueError('Вместительность не может быть меньше 1')

        self.weight = weight
        self.length = length
        self.capacity = capacity

    def print_info(self):
        """Метод печатает информацию об кровати."""
        print(f'Кровать размерами - {self.weight}X{self.length}\nВместительность: {self.capacity} чел.')

    def check_room(self, room_weight, room_length):
        """Метод анализирует, поместится ли кровать в комнате.
           Принимает на вход ширину и длину комнаты.
        """
        if not isinstance(room_weight, (int, float)):
            raise TypeError('Ширина комнаты может быть только целым или дробным числом!')
        if not isinstance(room_length, (int, float)):
            raise TypeError('Длина комнаты может быть только целым или дробным числом!')

        if room_weight < 0:
            raise ValueError('Ширина не может быть отрицательным числом!')
        if room_length < 0:
            raise ValueError('Длина не может быть отрицательным числом!')

        return self.weight < room_weight and self.length < room_length



if __name__ == "__main__":
    import doctest
    lada = Car('Лада', 120, 50000)
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest



