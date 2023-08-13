# Write your solution here
def all_the_longest(my_list:list):
    new = []
    longest = 0

    for i in my_list:
        if len(i) > longest:
           longest = len(i)
   
    for i in my_list:
        if len(i) == longest:
            new.append(i)
            
    return new

