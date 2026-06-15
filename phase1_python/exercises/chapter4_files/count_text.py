
def counts(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    print(f' Character: {len("".join(content.split()))} ')
    print(f' Words: {len(content.split())} ')
    print(f' Lines : {len(content.splitlines())} ')

fileName = input("Enter the file name: ")

print(f"{fileName} has exactly: \n ")
counts(fileName)