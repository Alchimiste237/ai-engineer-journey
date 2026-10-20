
test = ("chris", "prof", "dev", "age", "Dev")

profile = {"name": "Nathan", "age": 21,"proffession": "Dev" }

for prof in profile:
    # print(prof)

    if prof in test:
        print("hello world")


if test in profile:
    print("hello world")
