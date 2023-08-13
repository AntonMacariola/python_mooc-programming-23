list =[]
while True:
    print(f"The list is now {list}")
    ans = input("a(d)d, (r)emove or e(x)it: ").lower()
    if ans == 'd':
        list.append(len(list)+1)
    if ans == 'r':
        list.pop(-1)
    if ans == 'x':
        print('Bye!')
        break