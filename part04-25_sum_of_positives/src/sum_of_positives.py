# Write your solution here
def sum_of_positives(num_list: list):
    sum = 0
    for i in num_list:
        if i > 0 :
            sum = sum + i
    return sum

