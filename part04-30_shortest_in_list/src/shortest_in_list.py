# Write your solution here
def shortest(mylist: list):
    short = mylist[0]
    for i in mylist:
        if len(i) <= len(short):
            short = i
    return short
        
    