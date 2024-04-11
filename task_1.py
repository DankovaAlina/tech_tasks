#Задание: Написать функцию, которая принимает на вход
#список целых чисел и возвращает новый список,
#содержащий только уникальные элементы из исходного списка.

def get_unique_values(nums: list[int]) -> list[int]:
    return list(set(nums))
