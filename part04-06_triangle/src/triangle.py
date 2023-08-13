# Copy here code of line function from previous exercise
def line(char, hash):
    print(char * hash)
def triangle(size):
    # You should call function line here with proper parameters
    char = 1
    while char <= size:
        line(char, "#")
        char +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
