# Write your solution here
def length_of_longest(my_list: list):
    word = ""
    max_length = 0
    for i in my_list:
        if len(i) > max_length:
            max_length = len(i)
            word = i
    return len(word)
        