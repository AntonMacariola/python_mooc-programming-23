# Write your solution here
# You can test your function by calling it within the following block
def line(num, text):
    if text == "":
        text = "*"
    print(text[0] * num)
if __name__ == "__main__":
    line(5, "x")