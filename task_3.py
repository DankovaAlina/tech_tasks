#Создать класс Point, который представляет собой
#точку в двумерном пространстве.
#Класс должен иметь методы для инициализации координат точки,
#вычисления расстояния до другой точки, а также для получения и изменения координат.
from math import hypot


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_coords(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)

    def count_dist(self, point_2):
        p2_x, p2_y = point_2.get_coords()
        return hypot(p2_x - self.__x, p2_y - self.__y)
