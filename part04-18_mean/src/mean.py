# Write your solution here
# You can test your function by calling it within the following block

def mean(my_list):
    new_list = 0
    for i in range(len(my_list)):
        new_list = new_list + my_list[i]
    return new_list / len(my_list)  
    





if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)