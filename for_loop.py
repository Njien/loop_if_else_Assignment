import random

students = []

for i in range(1, 101):
    student = {
        "id": i,
        "name": f"Student{i}",
        "score": random.randint(0, 100)
    }
    students.append(student)

# Optional: print first 5 to preview
print(students)

