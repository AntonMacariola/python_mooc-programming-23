# Copy here code of line function from previous exercise
def line(size, character):
    print(size * character)
def square(size, character):
    counter = 0
    # You should call function line here with proper parameters
    while counter < size:
        line(size, character)
        counter += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")