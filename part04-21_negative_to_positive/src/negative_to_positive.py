# Write your solution here
user_input = int(input("Type a positive number: "))

for value in range(-user_input,(user_input + 1), 1):
    if value != 0:
        print(value)
