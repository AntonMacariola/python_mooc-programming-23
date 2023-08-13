# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(num, char):
    print(num * char)

def shape(num_1, char_1, num_2, char_2):
    str_1 = 1
    while str_1 <= num_1:
        line(str_1, char_1)
        str_1 +=1
    
    while num_2 > 0:
        line(num_1, char_2)
        num_2 -=1

if __name__ == "__main__":
    shape(5, "X", 3, "*")