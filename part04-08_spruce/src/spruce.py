# Write your solution here
# You can test your function by calling it within the following block

def spruce(num):
    print("a spruce!")
    i = 1
    while i <= num:
        print(" " * (num - i) + "*" * (2 * i - 1))
        i += 1
    print(" " * (num - 1) + "*")

if __name__ == "__main__":
    spruce(5)