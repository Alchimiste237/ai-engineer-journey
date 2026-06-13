print("============FizzBuzz program============")

for i in range(1, 51):
    if i < 3:
        continue  
    elif i % 3 == 0 and i % 5 == 0:
        print(f" {i} : FizzBuzz")
    elif i % 3 == 0:
        print(f" {i}: Fizz")
    elif i % 5 == 0:
        print(f" {i}: Buzz")
    else:
        print(f" {i}")