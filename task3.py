# Hайти средний балл по всем студентам и вывести имена студентов, чей балл выше среднего

# Структурная реализация

student_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95},
]

total_score = 0
for student in student_data:
    total_score += student['score']

average = total_score / len(student_data)

above_average_students = []
for student in student_data:
    if student['score'] > average:
        above_average_students.append(student['name'])

print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")