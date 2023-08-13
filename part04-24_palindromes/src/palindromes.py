# Write your solution here
def palindromes(n):
    if n == n[::-1]:
        return True
    else: 
        return False
    

def main():
    while True:
        user_input = input("Please type in a palindrome: ")
        if palindromes(user_input):
            print(f"{user_input} is a palindrome!")
            break
        print("that wasn't a palindrome")

main()

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
