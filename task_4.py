#Написать программу, которая сортирует список строк по длине,
#сначала по возрастанию, а затем по убыванию

def sort_list(str_list: list[str]) -> list[str]:
    for i in range(len(str_list) - 1):
        for k in range(i+1, len(str_list)):
            if len(str_list[i]) > len(str_list[k]):
                str_list[i], str_list[k] = str_list[k], str_list[i]
    return str_list[::-1]
