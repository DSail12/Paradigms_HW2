# Hайти средний балл по всем студентам и вывести имена студентов, чей балл выше среднего

# Процедурная реализация

student_data = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95},
]


def calculate_average(student_data):
    total_score = 0
    for student in student_data:
        total_score += student['score']
    return total_score / len(student_data)


def find_above_average_students(student_data, average):
    above_average_students = []
    for student in student_data:
        if student['score'] > average:
            above_average_students.append(student['name'])
    return above_average_students


average = calculate_average(student_data)
above_average_students = find_above_average_students(student_data, average)

print(f"Средний балл: {average}")
print(f"Студенты с баллом выше среднего: {above_average_students}")