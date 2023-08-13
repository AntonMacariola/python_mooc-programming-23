# Write your solution here
def even_numbers (num_list: list):
    new_list = []
    for value in num_list:
        if value % 2 == 0:
            new_list.append(value)
    return new_list
