# Write your solution here
# You can test your function by calling it within the following block
def first_word(s):
    """Returns the first word of the input string"""
    return s.split()[0]

def second_word(s):
    """Returns the second word of the input string"""
    return s.split()[1]

def last_word(s):
    """Returns the last word of the input string"""
    return s.split()[-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))