# Write your solution here
def anagrams(str_1,str_2):
    if sorted(str_1) == sorted(str_2):
        return True
    else:
        return False