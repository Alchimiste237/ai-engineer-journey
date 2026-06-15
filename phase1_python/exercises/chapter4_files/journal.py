print("===========Journal CLI ===========\n")

def display():
    with open("journal.txt", "r") as f:
        content = f.read()
    print(content)

def write():
    print("Enter text line by line and enter q to stop")
    contents = []
    while True:
        text = input(' ')
        if text.lower().lstrip() == "q":
            break
        contents.append(text + " \n")
    
    with open("journal.txt", "a") as f:
        for content in contents:
            f.write(content + " \n")
            
        
    

while True:
    print("type (d) display contents, (w) write content, (q) to quit \n")

    reponse = input(" ")
    # print(f"reponse: {reponse} . and after .lower:  {reponse.lower()} ")
    if reponse.lower().lstrip() == "d":
        display()
    elif reponse.lower().lstrip() == "w":
        write()
    elif reponse.lower().lstrip() == "q":
        print("See you later")
        break
    else:
        ("type (d) display content, (r) write content, (q) to quit \n")


