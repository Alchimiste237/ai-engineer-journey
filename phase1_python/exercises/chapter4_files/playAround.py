import json

with open("grade_summary.json", "r") as f:
    students = json.load(f)


students.append(
    {"name": "Junior","average": 99},
)

student = []
students.append(
    {"name": "Cyril","average": 97}
)
student.extend([1, 2, 3])
student.insert(1, 25)
print(student)
# students.remove({"name": "Junior","average": 99})
# student.remove()

store = {}
for student in students:
    if "Junior" in student["name"] :
        student["average"] = 101
        # print("find")

with open("grade_summary.json", "w") as f:
    json.dump(students, f, indent=2)

# student = 