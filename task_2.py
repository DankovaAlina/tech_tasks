#Написать функцию, которая принимает на вход
#два целых числа (минимум и максимум) и
#возвращает список всех простых чисел в заданном диапазоне.

def get_prime_nums(min_value: int, max_value: int) -> list[int]:
    if min_value < 1:
        min_value = 1
    if max_value < 1:
        return []
    numbers = list(range(min_value, max_value+1))
    prime_numbers = []
    is_prime = True
    for number in numbers:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
    return prime_numbers
