print("Returns the average of any number")

def average(*numbers):
    print(f"The average of these numbers: {numbers} is : {sum(numbers) / len(numbers)}")

average(10, 25, 56, 89)