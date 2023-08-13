# Write your solution here
def distinct_numbers(my_list: list):
    newlist=[]
    for i in my_list:
        if i not in newlist:
            newlist.append(i)
    return sorted(newlist)