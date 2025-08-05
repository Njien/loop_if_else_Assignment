import random

students = []
i = 1

while i <= 100:
    student = {
        "id": i,
        "name": f"Student{i}",
        "score": random.randint(0, 100)
    }
    students.append(student)
    i += 1

print(students)


