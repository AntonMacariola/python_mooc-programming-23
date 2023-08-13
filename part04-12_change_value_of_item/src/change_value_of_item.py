# Write your solution here
list = [1,2,3,4,5]
while True:   
    index = int(input("Index: "))
    if index < 0:
        break
    new_val = int(input("New Value: "))

    list[index] = new_val
    print(list)

           
