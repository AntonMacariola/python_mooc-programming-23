# Write your solution here
list = []
item = int(input("How many items: "))
n=1
while item >= n:
    list.append(int(input(f"Item {n}: ")))
    n+=1
print(list)