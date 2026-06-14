print("Print name each detail key-value pair")

def describe_person(name, **details):
    print(f"{name} description: age:jj {details['age']}")

describe_person("Chris", age=28, city="Yaounde")