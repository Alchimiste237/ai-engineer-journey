# without using Python's built-in [::-1]
print("=====================Reverse string function=====================")
string = input("Enter a word: ")

def reverse_string(string):
    reverse_text = ""
    for i in range(len(string) - 1, -1, -1):
        reverse_text += string[i]
    return reverse_text

print("the reverse text is: ")
print(reverse_string(string))