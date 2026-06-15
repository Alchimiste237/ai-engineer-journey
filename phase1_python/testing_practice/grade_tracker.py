import csv
import json

def load_students(filepath):
    # Load student data from CSV into a list of dicts

    students = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            students.append({
                "name": row["Name"],
                "math": int(row["Math"]),
                "science": int(row["Science"]),
                "english": int(row["English"])
            })
    return students

def calculate_average(students):

    scores = [students["math"], students["science"], students["english"] ]
    return sum(scores) / len(scores)

def build_summary(students):

    summary = []
    for student in students:
        avg = calculate_average(student)
        summary.append({
            "name": student["name"],
            "average": round(avg, 2)
        })
    
    summary.sort(key=lambda s: s["average"], reverse=True )
    return summary

def save_summary(summary, filepath):
    #save summary to a json file
    with open(filepath, "w") as f:
        json.dump(summary, f, indent=2 )
    print(f"Summary save to {filepath} succesfully")

def main():
    try:
        students = load_students("students.csv")
    except FileNotFoundError:
        print("students.csv not found. Make sure it's in this folder ")
        return
    
    summary = build_summary(students)
    save_summary(summary, "grade_summary.json")

    for entry in summary:
        print(f"{entry["name"]}: {entry['average']} ")

if __name__ == "__main__":
    main()
