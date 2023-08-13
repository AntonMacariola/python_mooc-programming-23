# Write your solution here
words = []
count = 0

while True:
    word = input("Enter a word: ")
    
    if word in words:
        print("You typed in", count, "different words")
        break
        
    words.append(word)
    count += 1

